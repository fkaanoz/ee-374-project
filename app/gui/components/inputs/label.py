from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel
   )

from gui.style.load_stylesheet import load_stylesheet

class Label(QWidget):
    def __init__(self, label=""):
        super().__init__()

        style_sh = load_stylesheet("inp_label.css")
        self.setStyleSheet(style_sh)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15,0,0,0)

        l = QLabel(label)
        layout.addWidget(l)