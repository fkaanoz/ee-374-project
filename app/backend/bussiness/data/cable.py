# It holds the database mapping. It is kinda dataclass.

class Cable():
    def __init__(self, cable_id=None, cable_code=None, line_to_neutral_voltage_level=None, line_to_line_voltage_level=None,
                current_capacity_flat=None, current_capacity_trefoil=None, resistance=None,
                inductance_flat=None, inductance_trefoil=None, capacitance=None, price=None):

            self.cable_id = cable_id
            self.cable_code = cable_code 
            self.line_to_neutral_voltage_level = line_to_neutral_voltage_level 
            self.line_to_line_voltage_level = line_to_line_voltage_level 
            self.current_capacity_flat = current_capacity_flat
            self.current_capacity_trefoil = current_capacity_trefoil 
            self.resistance = resistance 
            self.inductance_flat = inductance_flat
            self.inductance_trefoil = inductance_trefoil 
            self.capacitance = capacitance 
            self.price = price
            

    @classmethod        ## I used it for return Cable objects.
    def from_db_row_to_obj(cls, row):
          return cls( cable_id = row[0], cable_code = row[1], line_to_neutral_voltage_level= row[2], line_to_line_voltage_level= row[3], current_capacity_flat= row[4], current_capacity_trefoil= row[5], resistance= row[6], inductance_flat= row[7], inductance_trefoil= row[8], capacitance= row[9], price = row[10])