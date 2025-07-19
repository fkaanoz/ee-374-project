from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
   )

from PySide6.QtGui import QCursor, Qt

from gui.style.load_stylesheet import load_stylesheet


class CableSelectHeader(QWidget):
    def __init__(self):
        super().__init__()
        
        style_sh = load_stylesheet("cable_select_header.css")
        self.setStyleSheet(style_sh)
        
        layout = QHBoxLayout(self)

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(2)

        a = QLabel("Cable ID")
        a.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        b = QLabel("Cable Code")
        b.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        c = QLabel("Voltage Level (L-N)")
        c.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        d = QLabel("Voltage Level (L-L)")
        d.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        e = QLabel("Current Capacity")
        e.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


        layout.addWidget(a)
        layout.addWidget(b)
        layout.addWidget(c)
        layout.addWidget(d)
        layout.addWidget(e)
