from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
   )

from PySide6.QtCore import Qt, Signal

from gui.components.inputs.cable_length import CableLenInp


class CableLength(QWidget):
    input_changed = Signal(int)
    
    def __init__(self, sig, user_input, footer, cable_type_changed):
        super().__init__()
        self.cable_type_changed = cable_type_changed

        self.calc_sig = sig
        self.user_input = user_input
        self.footer = footer

        cable_length = QWidget()
        outer_layout = QHBoxLayout(cable_length)

        shp = QWidget()
        shp.setMinimumWidth(700)
        layout = QVBoxLayout(shp)
        layout.setContentsMargins(0, 0, 0, 70) 
        layout.setSpacing(0) 
        layout.setAlignment(Qt.AlignCenter | Qt.AlignCenter) 

        self.length = CableLenInp(input_changed = self.input_changed, user_input = self.user_input, cable_type_changed = self.cable_type_changed)

        layout.addWidget(self.length)


        outer_layout.addStretch()
        outer_layout.addWidget(shp)
        outer_layout.addStretch()

        self.setLayout(outer_layout)

        self.input_changed.connect(self.get_input)
        
    def get_input(self):
        cable_length = self.length.length_i.inp.value()
        nopc = self.length.nopc_i.inp.value()

        self.user_input["cable_length"] = {
                "length" : cable_length,
                "number_of_parallel_circuits" : nopc
        }


        