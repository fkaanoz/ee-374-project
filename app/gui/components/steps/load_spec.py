from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QFrame,
    QHBoxLayout
   )

from PySide6.QtCore import Qt, Signal

from gui.components.inputs.power_spec import PowerSpec
from gui.components.inputs.load_type import LoadType
from gui.components.inputs.voltage_level_spec import VoltageLevel


class LoadSpec(QWidget):
    input_changed = Signal(int)

    def __init__(self, sig, user_input):
        super().__init__()

        self.calc_sig = sig
        self.user_input = user_input

        load_spec = QWidget()
        load_spec.setMinimumWidth(500)
        outer_layout = QHBoxLayout(load_spec)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0) 
        layout.setAlignment(Qt.AlignCenter | Qt.AlignCenter) 
        
        self.voltage_level = VoltageLevel(input_changed=self.input_changed)
        self.power = PowerSpec(input_changed=self.input_changed)
        self.load_type = LoadType(input_changed=self.input_changed)

        layout.addWidget(self.voltage_level)
        layout.addWidget(self.power)
        layout.addWidget(self.load_type)
        
        outer_layout.addStretch()
        outer_layout.addLayout(layout)
        outer_layout.addStretch()

        self.setLayout(outer_layout)

        self.input_changed.connect(self.get_input)

    def get_input(self):
        voltage_level = self.voltage_level.voltage_i.inp.value()
        active_power = self.power.act_p.inp.value()
        reactive_power = self.power.reac_p.inp.value()
        load_type_id = self.load_type.button_group.checkedId()

        load_type = ""
        match load_type_id:
            case 1:
                load_type = "Industrial"
            case 2:
                load_type = "Residential"
            case 3:
                load_type = "Municipal"
            case 4:
                load_type = "Commercial"
            case _:
                load_type = ""


        self.user_input["load_spec"] = {
                "rated_voltage" : voltage_level,
                "active_power": active_power,
                "reactive_power" : reactive_power,
                "load_type" : load_type
        }


        