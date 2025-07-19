from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
   )

from gui.components.inputs.num_inp import NumericInp
from gui.components.inputs.label import Label

from gui.style.load_stylesheet import load_stylesheet

class VoltageLevel(QWidget):
    def __init__(self, input_changed):
        super().__init__()
        self.input_changed = input_changed

        style_sh = load_stylesheet("voltage_level_spec.css")
        self.setStyleSheet(style_sh)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,20,0,0)
        layout.setSpacing(0) 


        self.label = Label(label="Rated Voltage Level at the Load: ")
        layout.addWidget(self.label)

        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(0, 0, 0, 0) 
        inp_layout.setSpacing(0) 
        
        self.voltage_i = NumericInp(unit="Volt", lower_bound=0, sig=self.input_changed)

        inp_layout.addWidget(self.voltage_i)

        layout.addWidget(self.inp)

        self.setLayout(layout)