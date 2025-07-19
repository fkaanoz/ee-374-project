from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton
)

from PySide6.QtCore import QSize

from PySide6.QtGui import QIcon


from gui.style.load_stylesheet import load_stylesheet

class ClearButton(QWidget):
    def __init__(self, handler):
        super().__init__()

        style_sh = load_stylesheet("clear_button.css")
        self.setStyleSheet(style_sh)

        button = QPushButton("Clear and Go Back")
        button.setIcon(QIcon("_.png"))
        button.setIconSize(QSize(20, 20))
        
        button.clicked.connect(handler)
    
        layout = QHBoxLayout(self)

        layout.addWidget(button)

    