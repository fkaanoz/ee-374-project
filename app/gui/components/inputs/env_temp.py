from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    
   )

from gui.components.inputs.num_inp import NumericInp
from gui.components.inputs.label import Label

from gui.style.load_stylesheet import load_stylesheet

class EnvTemperature(QWidget):
    def __init__(self, input_changed):
        super().__init__()
        self.input_changed = input_changed

        style_sh = load_stylesheet("env_temp.css")
        self.setStyleSheet(style_sh)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,20,0,0)
        layout.setSpacing(0)

        self.label = Label(label="Environment Temperature :")
        layout.addWidget(self.label)

        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(0, 0, 0, 0) 
        inp_layout.setSpacing(0) 
        
        self.temp_i = NumericInp(unit="Celcius", lower_bound=-100, upper_bound=100, sig=self.input_changed)

        inp_layout.addWidget(self.temp_i)

        layout.addWidget(self.inp)

        self.setLayout(layout)