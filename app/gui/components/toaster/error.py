from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QTimer

from gui.style.load_stylesheet import load_stylesheet

class ErrorToast(QLabel):
    def __init__(self, msg, parent):
        super().__init__(parent)

        style_sh = load_stylesheet("toaster/error.css")
        self.setStyleSheet(style_sh)
        
        self.setText(msg)
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
    
        self.setMinimumHeight(40)
        self.setMinimumWidth(300)

        QTimer.singleShot(2000, self.close)
