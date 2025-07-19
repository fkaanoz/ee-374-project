from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QRadioButton,
    QButtonGroup
   )

from PySide6.QtCore import Signal
from gui.components.inputs.label import Label
from gui.style.load_stylesheet import load_stylesheet

class CableTypeSpec(QWidget):
    def __init__(self, input_changed, cable_type_changed):
        super().__init__()
        self.input_changed = input_changed
        self.cable_type_changed = cable_type_changed

        style_sh = load_stylesheet("cable_type_spec.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,10,0,0)
        layout.setSpacing(0)

        self.label = Label(label="Cable Type : ")
        self.label.setMinimumWidth(125)
        layout.addWidget(self.label)

        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(25, 0, 0, 0) 
        inp_layout.setSpacing(20) 
        
        self.single_core = QRadioButton("Single Core")
        self.three_core = QRadioButton("Three Core")

        self.button_group = QButtonGroup(self.inp)
        self.button_group.addButton(self.single_core, 1)
        self.button_group.addButton(self.three_core, 2)

    
        self.single_core.setChecked(True)
        
        self.button_group.idClicked.connect(self.on_cable_type_changed)

        inp_layout.addWidget(self.single_core)
        inp_layout.addWidget(self.three_core)
        inp_layout.addStretch()

        layout.addWidget(self.inp)

        self.setLayout(layout)

    def on_cable_type_changed(self, id):
        # print("cable type changed to", id)
        self.cable_type_changed.emit(id)
        self.input_changed.emit(id)
        
