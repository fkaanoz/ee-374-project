from PySide6.QtWidgets import (
    QHBoxLayout,
    QSpinBox,
    QWidget,
    QLabel
)

from PySide6.QtCore import Qt

from gui.style.load_stylesheet import load_stylesheet

class NumberOfPCInp(QWidget):
    def __init__(self, unit="", upper_bound=6, lower_bound=1, sig=None, cable_type_changed_sig=None, user_input=None):
        super().__init__()
        self.sig = sig
        self.user_input = user_input
        self.cable_type_changed_sig = cable_type_changed_sig

        style_sh = load_stylesheet("num_inp.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setSpacing(0)

        self.inp = QSpinBox()
        self.inp.setRange(lower_bound, upper_bound)  # 1 to 6
        self.inp.setSingleStep(1)
        self.inp.setButtonSymbols(QSpinBox.NoButtons)
        self.inp.setMinimumHeight(40)
        self.inp.setMinimumWidth(150)
        self.inp.setMaximumWidth(150)
        self.inp.setAlignment(Qt.AlignCenter)

        self.inp.valueChanged.connect(self.on_value_changed)

        self.label = QLabel(unit)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumWidth(180)
        self.label.setMaximumWidth(180)
        layout.addWidget(self.inp)
        layout.addWidget(self.label)
        layout.addStretch()

        self.setLayout(layout)

        self.cable_type_changed_sig.connect(self.set_upper_bound)

    def on_value_changed(self):
        if self.sig:
            self.sig.emit(1)   # just direct the signal!


    def set_upper_bound(self, id):
        max_nopc = 6 if id == 2 else 2
        print(f"max_nopc: {max_nopc}")
        self.inp.setMaximum(max_nopc)
        
        if max_nopc == 2:
            self.label.setText("max: 2 (for single-core)")
        else:
            self.label.setText("max: 6 (for three-core)")
    
