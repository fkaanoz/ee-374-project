from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QRadioButton,
    QButtonGroup,
    QVBoxLayout
   )

from gui.components.inputs.label import Label

from gui.style.load_stylesheet import load_stylesheet

from PySide6.QtCore import Qt

class LoadType(QWidget):
    def __init__(self, input_changed):
        super().__init__()
        self.input_changed = input_changed


        style_sh = load_stylesheet("load_type.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        
        layout.setSpacing(0) 

        label = Label(label="Load Type : ")
        layout.addWidget(label)

        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(0, 5, 0, 0) 
        inp_layout.setSpacing(20) 
        inp_layout.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        self.ind_load = QRadioButton("Industrial")
        self.res_load = QRadioButton("Residential")
        self.mun_load = QRadioButton("Municipal")
        self.comm_load = QRadioButton("Commercial")

        self.button_group = QButtonGroup(self.inp)
        self.button_group.addButton(self.ind_load, 1)
        self.button_group.addButton(self.res_load, 2)
        self.button_group.addButton(self.mun_load, 3)
        self.button_group.addButton(self.comm_load, 4)

        self.button_group.idClicked.connect(self.on_load_type_changed)

        self.ind_load.setChecked(True)

        inp_layout.addStretch()
        inp_layout.addWidget(self.ind_load)
        inp_layout.addWidget(self.res_load)
        inp_layout.addWidget(self.mun_load)
        inp_layout.addWidget(self.comm_load)
        inp_layout.addStretch()

        layout.addWidget(self.inp)

        self.setLayout(layout)

    def on_load_type_changed(self, id):
        self.input_changed.emit(id)