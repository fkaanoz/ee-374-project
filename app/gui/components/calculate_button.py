from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton
)

from gui.style.load_stylesheet import load_stylesheet

class CalculateButton(QWidget):
    def __init__(self):
        super().__init__()

        button = QPushButton("CALCULATE")

        style_sh = load_stylesheet("calculate_button.css")
        button.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)

        layout.addWidget(button)

    