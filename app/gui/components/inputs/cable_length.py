from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    
   )

from gui.components.inputs.num_inp import NumericInp
from gui.components.inputs.num_of_pc import NumberOfPCInp
from gui.components.inputs.label import Label

from gui.style.load_stylesheet import load_stylesheet

class CableLenInp(QWidget):
    def __init__(self, input_changed, user_input, cable_type_changed=None):
        self.user_input = user_input
        super().__init__()
        self.input_changed = input_changed
        self.cable_type_changed = cable_type_changed

        style_sh = load_stylesheet("cable_length_inp.css")
        self.setStyleSheet(style_sh)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,20,0,0)
        layout.setSpacing(0)

        self.cl_label = Label(label="Cable Length (km) :")
        layout.addWidget(self.cl_label)

        # input for cable length
        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(0, 0, 0, 30) 
        inp_layout.setSpacing(0) 
        
        self.length_i = NumericInp(unit="km", lower_bound=0, upper_bound=10_000, sig=self.input_changed)

        inp_layout.addWidget(self.length_i)

        layout.addWidget(self.inp)

        self.nopc_label = Label(label="Number of Parallel Circuit :")
        layout.addWidget(self.nopc_label)

        # input for number of parallel circuit
        self.nopc = QWidget()
        nopc_layout = QHBoxLayout(self.nopc)
        nopc_layout.setContentsMargins(0, 0, 0, 0)
        nopc_layout.setSpacing(0)
        
        
        self.nopc_i = NumberOfPCInp(unit="max: 2 (for single-core)", lower_bound=1, upper_bound=2, sig=self.input_changed, cable_type_changed_sig=self.cable_type_changed, user_input=self.user_input)

        nopc_layout.addWidget(self.nopc_i)
        layout.addWidget(self.nopc)

        self.setLayout(layout)