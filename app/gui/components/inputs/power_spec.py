from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QVBoxLayout
   )

from gui.components.inputs.num_inp import NumericInp
from gui.components.inputs.label import Label

from gui.style.load_stylesheet import load_stylesheet

class PowerSpec(QWidget):
    def __init__(self,input_changed):
        super().__init__()
        self.input_changed = input_changed

        style_sh = load_stylesheet("power_spec.css")
        self.setStyleSheet(style_sh)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,20,0,0)
        layout.setSpacing(0) 

        label = Label(label="Demanded Power by the Load: ")
        layout.addWidget(label)

        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(0, 0, 0, 0) 
        inp_layout.setSpacing(0) 
        
        self.act_p = NumericInp(unit="kW", sig=self.input_changed)
        self.reac_p = NumericInp(unit="kVAR", sig=self.input_changed)

        inp_layout.addWidget(self.act_p)
        inp_layout.addWidget(self.reac_p)

        layout.addWidget(self.inp)

        self.setLayout(layout)