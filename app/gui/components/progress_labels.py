from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)

from PySide6.QtCore import Qt

from gui.style.load_stylesheet import load_stylesheet

class ProgressLabel(QWidget):
    def __init__(self, step, index):
        super().__init__()

        self.index = index

        self.style_sh = load_stylesheet("progress.css")
        self.setStyleSheet(self.style_sh)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0) 
        

        self.label = QLabel(step)
        self.label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        layout.addWidget(self.label)

    def step_changed(self, index):
        if  self.index < index:
            self.label.setProperty("class", "passedStep")
        elif index == self.index:
            self.label.setProperty("class", "currentStep")
        else:
            self.label.setProperty("class","")

        self.label.style().unpolish(self.label) 
        self.label.style().polish(self.label)   
        self.label.update()
