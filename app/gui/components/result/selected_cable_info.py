from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
   )

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy

from backend.database.queries import Get_Cable_Code

from gui.style.load_stylesheet import load_stylesheet


class SelectedCableInfo(QWidget):
    def __init__(self, user_input, done_signal):
        super().__init__()

        style_sh = load_stylesheet("selected_cable_info.css")
        self.setStyleSheet(style_sh)

        self.user_input = user_input
        self.done_signal = done_signal

        layout = QVBoxLayout(self)
        
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        
        layout.setSpacing(0)

        label = QLabel("1. Summary of Your Selection : ")
        label.setStyleSheet("font-size: 15px; font-weight: bold; padding: 5px; padding-left: 10px; padding-right: 10px; border: 0px solid white")
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setContentsMargins(0, 0, 0, 0)
        
        layout.addWidget(label)

        sum_widget = QWidget(self)

        sum_layout = QHBoxLayout(sum_widget)
        sum_layout.setContentsMargins(20, 0, 0, 0)
        sum_layout.setSpacing(0)
        self.rated_voltage = QLabel(f"Rated Voltage : {self.user_input["load_spec"]["rated_voltage"]} V")
        self.power_load = QLabel(f"Power@Load : {self.user_input["load_spec"]["active_power"]} KW  & {self.user_input["load_spec"]["reactive_power"]} KVAR")
        self.load_type = QLabel(f"Load Type : {self.user_input["load_spec"]["load_type"]}")
        self.cable_code = QLabel(f"Code: {self.user_input["cable_selection"]["cable_id"]}")
        self.cable_length = QLabel(f"Length: {self.user_input["cable_length"]["length"]} km")
        self.num_of_parallel = QLabel(f"# Par.Circuit: {self.user_input["cable_length"]["number_of_parallel_circuits"]}")
        
        sum_layout.addWidget(self.rated_voltage)
        sum_layout.addWidget(self.power_load)
        sum_layout.addWidget(self.load_type)
        sum_layout.addWidget(self.cable_code) 
        sum_layout.addWidget(self.cable_length)
        sum_layout.addWidget(self.num_of_parallel)
        sum_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        layout.addWidget(sum_widget)

        self.done_signal.connect(self.update_info)

    def update_info(self):
        cable_code = Get_Cable_Code(self.user_input["cable_selection"]["cable_id"])

        self.rated_voltage.setText(f"Rated Voltage: {self.user_input['load_spec']['rated_voltage']} V")
        self.power_load.setText(f"Power@Load: {self.user_input['load_spec']['active_power']} KW & {self.user_input['load_spec']['reactive_power']} KVAR")
        self.load_type.setText(f"Load Type: {self.user_input['load_spec']['load_type']}")
        self.cable_code.setText(f"Cable Code: {cable_code}")
        self.cable_length.setText(f"Cable Length: {self.user_input['cable_length']['length']} km")
        self.num_of_parallel.setText(f"# Par.Circuit: {self.user_input['cable_length']['number_of_parallel_circuits']}")
