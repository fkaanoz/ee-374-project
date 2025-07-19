from backend.database.queries import select_from_db
from backend.database.queries import Get_Resistance_Of_Cable
from backend.database.queries import Get_Capacitance_Of_Cable
from backend.database.queries import Get_Inductance_Of_Cable

import math

MAX_CABLE = 6
MNOC_SINGLE = 2
MNOC_THREE = 6
FREQUENCY = 50 

# used for smart listing algo!
def Find_Proper_Cables(user_input):
    # sanity check 
    if user_input["load_spec"]["rated_voltage"] == None:
        return []

    # inputs
    rated_voltage =  user_input["load_spec"]["rated_voltage"]
    active_power = user_input["load_spec"]["active_power"]
    reactive_power = user_input["load_spec"]["reactive_power"]

    cable_type = user_input["type_env"]["cable_type"]
    placement = user_input["type_env"]["placement"]
    environment_temp = user_input["type_env"]["env_temp"]

    apparent_power = calculate_apparent_power(active_power * 1000, reactive_power * 1000)
    load_current = apparent_power / (rated_voltage * math.sqrt(3))          # 230 in example

    # current should line carry :   => 242.1 in example
    total_current_should_carry = load_current / calculate_temp_correction(environment_temp)

    if cable_type == "Single Core" and placement == "Flat":
        each_circuit_min_current = total_current_should_carry / MNOC_SINGLE         # 242.1 / 2 in example
        lower_bound_for_flat_current_SC =  each_circuit_min_current / calculate_reduction_due_to_trench(MAX_CABLE)
        results = select_from_db(cable_type=cable_type, desired_voltage_level=rated_voltage, placement=placement, min_curr=lower_bound_for_flat_current_SC)
        return results


    elif cable_type == "Single Core" and placement == "Trefoil":
        each_circuit_min_current = total_current_should_carry / MNOC_SINGLE         # 242.1 / 2 in example      
        lower_bound_for_trefoil_current_SC = each_circuit_min_current / calculate_reduction_due_to_trench(MAX_CABLE)
        results = select_from_db(cable_type=cable_type, desired_voltage_level=rated_voltage, placement=placement, min_curr=lower_bound_for_trefoil_current_SC)
        return results
    

    else: # corresponds to Three Core and Trefoil case
        each_circuit_min_current = total_current_should_carry / MNOC_THREE         # 242.1 / 2 in example      
        lower_bound_for_trefoil_current_3C = each_circuit_min_current / calculate_reduction_due_to_trench(MAX_CABLE)
        results = select_from_db(cable_type=cable_type, desired_voltage_level=rated_voltage, placement=placement, min_curr=lower_bound_for_trefoil_current_3C)
    
        return results
    

def calculate_apparent_power(active, reactive):
    return math.sqrt(active * active + reactive * reactive)

# give correction factor between  1.15 and 0.8  => Linear
def calculate_temp_correction(temp_level):
    slope = - 0.05 / 5  # slope of the line => (1.15, 5) and (1.10, 10) points that passes through
    correction = slope * temp_level + 1.2         # 10 * (slope) + k = 1.10   => k = 1.2
    return correction

# table 2  => non-linear
def calculate_reduction_due_to_trench(num_of_cables):
     match num_of_cables:
        case 1:
            return 1
        case 2:
            return 0.90
        case 3:
            return 0.85
        case 4:
             return 0.80
        case 5:
             return 0.75
        case 6:
             return 0.70
        case _:
             return 0

# return in MW !!!! Important !!! 
def Calculate_Active_Losses(user_input):
    capacitance_per = Get_Capacitance_Of_Cable(user_input["cable_selection"]["cable_id"])

    match capacitance_per:
        case None:
            return Calculate_Active_Losses_with_Short_Line_Model(user_input)
        case _:
            return Calculate_Active_Losses_with_Medium_Line_Model(user_input, capacitance_per)


def Which_Model(user_input):
    capacitance_per = Get_Capacitance_Of_Cable(user_input["cable_selection"]["cable_id"])

    match capacitance_per:
        case None:
            return "Short Line Model"
        case _:
            return "Medium Line Model"


def Calculate_IR_at_Load(user_input):
    # sanity check 
    if user_input["load_spec"]["rated_voltage"] == None:
        return []

    # inputs
    rated_voltage =  user_input["load_spec"]["rated_voltage"]
    active_power = user_input["load_spec"]["active_power"]
    reactive_power = user_input["load_spec"]["reactive_power"]

    complex_power = complex(active_power * 1000, reactive_power * 1000)
    I_r = complex_power / (rated_voltage * math.sqrt(3))

    return I_r



def Calculate_Active_Losses_with_Medium_Line_Model(user_input, capacitance_per):
    (resistance_per, inductance_per) = Extract_Resistance_and_Inductance(user_input)

    # in ohms and in henries
    Z_param = (resistance_per + 1j*2*math.pi*FREQUENCY*inductance_per*(1/1000))  * (user_input["cable_length"]["length"])
    # C_param = capacitance_per * (user_input["cable_length"]["length"])
    Y_shunt = 1j * 2 * math.pi * FREQUENCY * (capacitance_per * 1e-6) * user_input["cable_length"]["length"]

    
    I_r = Calculate_IR_at_Load(user_input)
    I_r = I_r / user_input["cable_length"]["number_of_parallel_circuits"]  # in amperes

    V_r = user_input["load_spec"]["rated_voltage"]
    
    I_ab = V_r * (Y_shunt / 2) 

    I = I_r - math.sqrt(3) * I_ab

    active_power_loss_per_circuit = 3 * (abs(I)**2) * Z_param.real # in watts => ! return in MW

    active_power_loss = active_power_loss_per_circuit * user_input["cable_length"]["number_of_parallel_circuits"] 

    return active_power_loss / 1e6  # convert to MW


def Calculate_Active_Losses_with_Short_Line_Model(user_input):
    (resistance_per, inductance_per) = Extract_Resistance_and_Inductance(user_input)

    # in ohms and in henries
    total_impedance = (resistance_per + 1j*2*math.pi*FREQUENCY*inductance_per*(1/1000))  * (user_input["cable_length"]["length"])

    current_at_load = Calculate_Current_at_Load(user_input)

    current_per_circuit = current_at_load / user_input["cable_length"]["number_of_parallel_circuits"]  # in amperes

    active_power_loss_per_circuit = 3 * (current_per_circuit**2) * total_impedance.real # in watts => ! return in MW

    active_power_loss = active_power_loss_per_circuit * user_input["cable_length"]["number_of_parallel_circuits"] 

    return active_power_loss / 1e6  # convert to MW

def Extract_Resistance_and_Inductance(user_input):
    resistance_per = Get_Resistance_Of_Cable(user_input["cable_selection"]["cable_id"])
    
    placement = ""
    if user_input["type_env"]["cable_type"] == "Single Core":
        placement = user_input["type_env"]["placement"]
    else:
        placement = "Trefoil"

    inductance_per = Get_Inductance_Of_Cable(user_input["cable_selection"]["cable_id"], placement)

    return (resistance_per, inductance_per)
    
def Calculate_Current_at_Load(user_input):
    # sanity check 
    if user_input["load_spec"]["rated_voltage"] == None:
        return []

    # inputs
    rated_voltage =  user_input["load_spec"]["rated_voltage"]
    active_power = user_input["load_spec"]["active_power"]
    reactive_power = user_input["load_spec"]["reactive_power"]

    apparent_power = calculate_apparent_power(active_power * 1000, reactive_power * 1000)
    load_current = apparent_power / (rated_voltage * math.sqrt(3))          # 230 in example

    return load_current



# # Calculate Reactive Losses in MVAr !!!!
def Calculate_Reactive_Losses(user_input):
    capacitance_per = Get_Capacitance_Of_Cable(user_input["cable_selection"]["cable_id"])

    match capacitance_per:
        case None:
            return Calculate_Reactive_Losses_with_Short_Line_Model(user_input)
        case _:
            return Calculate_Reactive_Losses_with_Short_Line_Model(user_input)


def Calculate_Reactive_Losses_with_Medium_Line_Model(user_input, capacitance_per):
    (resistance_per, inductance_per) = Extract_Resistance_and_Inductance(user_input)

    Z_param = (resistance_per + 1j*2*math.pi*FREQUENCY*inductance_per*(1/1000)) * (user_input["cable_length"]["length"])
    Y_shunt = 1j * 2 * math.pi * FREQUENCY * (capacitance_per * 1e-6) * user_input["cable_length"]["length"]
    
    I_r = Calculate_IR_at_Load(user_input)
    I_r = I_r / user_input["cable_length"]["number_of_parallel_circuits"]

    V_r = user_input["load_spec"]["rated_voltage"]
    
    I_ab = V_r * (Y_shunt / 2) 

    I = I_r - math.sqrt(3) * I_ab

    V_s = V_r + Z_param * (I)

    I_cd = V_s * (Y_shunt / 2)

    reactive_power_loss_per_circuit = 3 * (abs(I)**2) * Z_param.imag + 3 * (abs(I_ab)**2) * (2 / Y_shunt).imag + 3 * (abs(I_cd)**2) * (2 / Y_shunt).imag

    reactive_power_loss = reactive_power_loss_per_circuit * user_input["cable_length"]["number_of_parallel_circuits"] 

    return reactive_power_loss / 1e6


def Calculate_Reactive_Losses_with_Short_Line_Model(user_input):
    (resistance_per, inductance_per) = Extract_Resistance_and_Inductance(user_input)

    # in ohms and in henries
    total_impedance = (resistance_per + 1j*2*math.pi*FREQUENCY*inductance_per*(1/1000))  * (user_input["cable_length"]["length"])

    current_at_load = Calculate_Current_at_Load(user_input)

    current_per_circuit = current_at_load / user_input["cable_length"]["number_of_parallel_circuits"]  # in amperes

    reactive_power_loss_per_circuit = 3 * (current_per_circuit**2) * total_impedance.imag

    reactive_power_loss = reactive_power_loss_per_circuit * user_input["cable_length"]["number_of_parallel_circuits"] 

    return reactive_power_loss / 1e6  # convert to MVAr

def Calculate_Voltage_Regulation(user_input):

    rated_voltage_ll = user_input["load_spec"]["rated_voltage"]  
    rated_voltage_ph = rated_voltage_ll / math.sqrt(3)           

    active_power = user_input["load_spec"]["active_power"] * 1000  # Watts
    reactive_power = user_input["load_spec"]["reactive_power"] * 1000  # VAR
    length_km = user_input["cable_length"]["length"]
    num_parallel = user_input["cable_length"]["number_of_parallel_circuits"]

    resistance_per, inductance_per = Extract_Resistance_and_Inductance(user_input)

    inductance_per = inductance_per / 1000  ## H/km

    total_impedance = complex(resistance_per, 2 * math.pi * FREQUENCY * inductance_per) * length_km

    apparent_power = complex(active_power, reactive_power)
    per_phase_S = apparent_power / 3
    load_current = per_phase_S.conjugate() / rated_voltage_ph 
    load_current = load_current / num_parallel 

    # voltage drop amount
    voltage_drop = load_current * total_impedance

    # source voltage = load + drop
    load_voltage = complex(rated_voltage_ph, 0)
    source_voltage = load_voltage + voltage_drop

    voltage_regulation = (abs(source_voltage) - abs(load_voltage)) / abs(load_voltage) * 100

    return voltage_regulation