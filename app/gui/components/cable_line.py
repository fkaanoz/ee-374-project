from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt
from gui.style.load_stylesheet import load_stylesheet

class CableLine(QWidget):
    def __init__(self, data):
        super().__init__()

        style_sh = load_stylesheet("cable_line_labels.css")
        self.setStyleSheet(style_sh)


        layout = QHBoxLayout(self)
        a = QLabel(str(data.cable_id)  if data.cable_id != None else "-")
        a.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        a.setProperty("class", "cableID")
    
        b = QLabel(str(data.cable_code) if data.cable_code != None else "-")
        b.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        c = QLabel(str(data.line_to_neutral_voltage_level) + " V" if data.line_to_neutral_voltage_level != None else "-")
        c.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        d = QLabel(str(data.line_to_line_voltage_level) + " V" if data.line_to_line_voltage_level != None else "-")
        d.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        e = QLabel(str(data.current_capacity_flat) + " A" if data.current_capacity_flat != None else "-")
        e.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        f = QLabel(str(data.current_capacity_trefoil) + " A" if data.current_capacity_trefoil != None else "-")
        f.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        g = QLabel(str(data.resistance) + " ohm/km" if data.resistance != None else "-")
        g.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        h = QLabel(str(data.inductance_flat) + " mH/km" if data.inductance_flat != None else "-")
        h.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        h1 = QLabel(str(data.inductance_trefoil) + " mH/km" if data.inductance_trefoil != None else "-")
        h1.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        h2 = QLabel(str(data.capacitance) + " uF/km" if data.capacitance != None else "-")
        h2.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        h3 = QLabel(str(data.price) + " TL/km" if data.price != None else "-")
        h3.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)


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
        
        # self.setMinimumHeight(40)


    