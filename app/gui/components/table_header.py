from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt
from gui.style.load_stylesheet import load_stylesheet

class TableHeader(QWidget):
    def __init__(self):
        super().__init__()

        style_sh = load_stylesheet("table_header.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        
        a = QLabel("Cable ID")
        a.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        b = QLabel("Cable Code")
        b.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        b.setProperty("class","evenLabels")
        
        c = QLabel("Voltage L-to-N")
        c.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        d = QLabel("Voltage L-to-L")
        d.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        d.setProperty("class","evenLabels")
        
        e = QLabel("Current Cap. (Fl)")
        e.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        f = QLabel("Current Cap. (Tr)")
        f.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        f.setProperty("class","evenLabels")
        
        g = QLabel("Resistance")
        g.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        h = QLabel("Inductance (Fl)")
        h.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        h.setProperty("class","evenLabels")
        
        h1 = QLabel("Inductance (Tr)")
        h1.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        
        h2 = QLabel("Capacitance")
        h2.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        h2.setProperty("class","evenLabels")
        
        h3 = QLabel("Price")
        h3.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        h4 = QLabel("")
        h4.setProperty("class","emptyLabel")


        h4.setMaximumWidth(25)

        layout.addWidget(a)
        layout.addWidget(b)
        layout.addWidget(c)

        layout.addWidget(d)
        layout.addWidget(e)
        layout.addWidget(f)

        layout.addWidget(g)
        layout.addWidget(h)
        layout.addWidget(h1)
        layout.addWidget(h2)
        layout.addWidget(h3)
        layout.addWidget(h4)
        

        self.setMinimumHeight(40)


    