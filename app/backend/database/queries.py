import sqlite3

from backend.bussiness.data.cable import Cable
from backend.database.db import connect_database

def Get_All_Cables():
    cur = connect_database()
    cur.execute("SELECT * FROM cables")
    
    rows = cur.fetchall()
    
    cables = []
    for r in rows:
        a = Cable.from_db_row_to_obj(r)
        cables.append(a)
    return cables


def select_from_db(cable_type, desired_voltage_level, placement, min_curr):
    cur = connect_database()

    select_temp = """
        SELECT * FROM cables WHERE 1=1
    """

    cable_type_prefix = "3x" if cable_type == "Three Core" else "1x"
    like_pattern = f"{cable_type_prefix}%"
    select_temp = select_temp + " AND cable_code LIKE ?" 


    # to get ride too much isolation & low isolation 
    quantized_voltage_level = quantize_voltage_levels(desired_voltage_level)
    select_temp = select_temp + " AND line_to_line_voltage_level = ?"


    if cable_type == "Three Core":
        select_temp = select_temp + " AND current_capacity_trefoil >= ?"
    elif cable_type == "Single Core" and placement == "Flat":
        select_temp = select_temp + " AND current_capacity_flat >= ?"
    elif cable_type == "Single Core" and placement == "Trefoil":
        select_temp = select_temp + " AND current_capacity_trefoil >= ?"
    else:
        print("SOMETHING REALY BAD")


    cur.execute(select_temp, (like_pattern, quantized_voltage_level, min_curr))
    results = cur.fetchall()

    return results


def quantize_voltage_levels(desired_voltage_level):
    quant = 0.0
    match desired_voltage_level:
        case voltage if 0.0 <= voltage <= 1000.0:
            quant = 1000
        case voltage if 1000.0 < voltage <= 6000.0:
            quant = 6000
        case voltage if 6000.0 < voltage <= 10000.0:
            quant = 10000
        case voltage if 10000.0 < voltage <= 20000.0:
            quant = 20000
        case voltage if 20000.0 < voltage <= 35000.0:
            quant = 35000
        case _:
            quant = None
    return quant


def Get_Cable_Code(id):
    cur = connect_database()
    cur.execute("SELECT cable_code FROM cables WHERE cable_id = ?", (id,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None


def Get_Price_Of_Cable(id):
    cur = connect_database()
    cur.execute("SELECT price FROM cables WHERE cable_id = ?", (id,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None


def Get_Resistance_Of_Cable(id):
    cur = connect_database()
    cur.execute("SELECT resistance FROM cables WHERE cable_id = ?", (id,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None


def Get_Capacitance_Of_Cable(id):
    cur = connect_database()
    cur.execute("SELECT capacitance FROM cables WHERE cable_id = ?", (id,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None


def Get_Inductance_Of_Cable(id, placement):
    cur = connect_database()

    if placement == "Flat":
        cur.execute("SELECT inductance_flat FROM cables WHERE cable_id = ?", (id,))
        result = cur.fetchone()
    else:
        cur.execute("SELECT inductance_trefoil FROM cables WHERE cable_id = ?", (id,))
        result = cur.fetchone()
    
    
    if result:
        return result[0]
    else:
        return None