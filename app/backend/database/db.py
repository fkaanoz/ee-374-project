import sqlite3
import os
import re
import sys


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)


def extract_voltage_levels(voltage_str):
    match = re.search(r"(\d*\.?\d+)/(\d+) kV", voltage_str)

    if match:
        line_to_neutral_voltage_level = float(match.group(1))
        line_to_line_voltage_level = float(match.group(2))
        return int(line_to_neutral_voltage_level * 1000), int( line_to_line_voltage_level *1000)
    else:
        return None, None


# singleton for connection !
conn = None
def connect_database():
    global conn
    if conn != None:
        return conn.cursor()
    
    db_path = resource_path("cables.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return cur


# def seed_database():
#     cur = connect_database()

#     cur.execute("DROP TABLE IF EXISTS cables")          # do not afraid!
#     cur.execute("CREATE TABLE cables(cable_id INTEGER PRIMARY KEY UNIQUE, cable_code TEXT NOT NULL, line_to_neutral_voltage_level INTEGER NOT NULL, line_to_line_voltage_level INTEGER NOT NULL, current_capacity_flat INTEGER, current_capacity_trefoil INTEGER NOT NULL, resistance REAL NOT NULL, inductance_flat REAL, inductance_trefoil REAL NOT NULL, capacitance REAL, price INTEGER NOT NULL)")
    
#     sql_statement_template = """
#             INSERT INTO cables (
#                 cable_id, cable_code, line_to_neutral_voltage_level, line_to_line_voltage_level,
#                 current_capacity_flat, current_capacity_trefoil, resistance,
#                 inductance_flat, inductance_trefoil, capacitance, price
#             ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """
    
#     df= pd.read_excel("cables.xlsx", header=1)

#     for index, row in df.iterrows():
#         cable_id = row["Cable ID"]
#         cable_code = row["Cable code"]
#         line_to_neutral_voltage_level, line_to_line_voltage_level = extract_voltage_levels(row["Voltage level"])

#         current_capacity_flat = row["Current Capacity (A) at 20°C ..."]
#         current_capacity_trefoil = row["Current Capacity (A) at 20°C :."]
#         resistance = row["Resistance (ohm/km)"]
#         inductance_flat = row["Inductance ... (mH/km)"]
#         inductance_trefoil = row["Inductance :. (mH/km)"]
#         capacitance = row["Capacitance (uF/km)"]
#         price = row["Price (TL/km)"]

#         cur.execute(sql_statement_template, (
#                 cable_id, cable_code, line_to_neutral_voltage_level, line_to_line_voltage_level,
#                 current_capacity_flat, current_capacity_trefoil, resistance,
#                 inductance_flat, inductance_trefoil, capacitance, price
#         ))

#     conn.commit()
#     print("Cable data added to the database.")

# seed_database()