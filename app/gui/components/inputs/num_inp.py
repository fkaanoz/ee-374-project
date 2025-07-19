from PySide6.QtWidgets import (
    QHBoxLayout,
    QDoubleSpinBox,
    QWidget,
    QLabel
)

from PySide6.QtCore import Qt

from gui.style.load_stylesheet import load_stylesheet

class NumericInp(QWidget):

    def __init__(self, unit="", upper_bound=100_000, lower_bound=-100_000, sig=None):
        super().__init__()
        self.sig = sig

        style_sh = load_stylesheet("num_inp.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setSpacing(0)

        self.inp = QDoubleSpinBox()
        self.inp.setRange(lower_bound, upper_bound)
        self.inp.setDecimals(2)
        self.inp.setSingleStep(0.1)
        self.inp.setButtonSymbols(QDoubleSpinBox.NoButtons)
        self.inp.setMinimumHeight(40)
        self.inp.setMinimumWidth(250)
        self.inp.setMaximumWidth(250)
        self.inp.setAlignment(Qt.AlignCenter)

        self.inp.valueChanged.connect(self.on_value_changed)

        self.label = QLabel(unit)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumWidth(80)
        self.label.setMaximumWidth(80)
        layout.addWidget(self.inp)
        layout.addWidget(self.label)
        layout.addStretch()


        self.setLayout(layout)

    def on_value_changed(self):
        self.sig.emit(1)   # just direct the signal!