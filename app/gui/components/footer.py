from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)
from PySide6.QtCore import Qt
from gui.style.load_stylesheet import load_stylesheet

class Footer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) 
        
        self.footer = QLabel("power-cable-ui - v1.1.0")

        style_sh = load_stylesheet("footer.css")
        self.footer.setStyleSheet(style_sh)

        self.footer.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)         
        self.footer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.footer)