from PySide6.QtWidgets import (QLabel,QWidget, QHBoxLayout)
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation

from gui.style.load_stylesheet import load_stylesheet

class SuccessToast(QWidget):
    def __init__(self, msg, parent):
        super().__init__(parent)
        self.setProperty("class", "SuccessToaster")
        self.setAttribute(Qt.WA_StyledBackground, True)

        layout = QHBoxLayout(self)

        style_sh = load_stylesheet("toaster/success.css")
        self.setStyleSheet(style_sh)
        
        self.label = QLabel(msg)

        self.label.setText(msg)

        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )


        par_rect = parent.geometry()
        self.setMaximumHeight(par_rect.height())
        self.setMinimumWidth(par_rect.width())

        QTimer.singleShot(2500, self.fade_out_anim)

    def fade_out_anim(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(350) 
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.finished.connect(self.close)
        self.anim.start()