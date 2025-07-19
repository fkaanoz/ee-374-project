from PySide6.QtWidgets import (    
    QWidget,
    QHBoxLayout,
    QRadioButton,
    QButtonGroup
   )


from gui.components.inputs.label import Label

from gui.style.load_stylesheet import load_stylesheet

class PlacementSpec(QWidget):
    def __init__(self, input_changed):
        super().__init__()

        self.input_changed = input_changed

        style_sh = load_stylesheet("placement_spec.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,10,0,0)
        layout.setSpacing(0)

        label = Label(label="Placement : ")
        label.setMinimumWidth(125)
        layout.addWidget(label)

        self.inp = QWidget()
        inp_layout = QHBoxLayout(self.inp)
        inp_layout.setContentsMargins(25, 0, 0, 0) 
        inp_layout.setSpacing(20) 
        
        self.flat = QRadioButton("Flat")
        self.trefoil = QRadioButton("Trefoil")

        self.button_group = QButtonGroup(self.inp)
        self.button_group.addButton(self.flat, 1)
        self.button_group.addButton(self.trefoil, 2)


        self.button_group.idClicked.connect(self.on_placement_changed)

        self.flat.setChecked(True)

        inp_layout.addWidget(self.flat)
        inp_layout.addWidget(self.trefoil)
        inp_layout.addStretch()

        layout.addWidget(self.inp)

        self.setLayout(layout)


    def on_placement_changed(self,id):
        self.input_changed.emit(id)