from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)

from PySide6.QtGui import QCursor, Qt

from PySide6.QtCore import Qt, Signal
from gui.style.load_stylesheet import load_stylesheet

class CableSelectLine(QWidget):
    def __init__(self,id, data, sig:Signal, user_data):
        super().__init__()
        self.id = id
        self.sig = sig
        self.is_selected = False

        self.user_data = user_data

        self.outer_wg = QWidget()
        self.outer_wg.setProperty("class", "outer")

        self.original_cursor = self.cursor()

        style_sh = load_stylesheet("cable_select_line.css")
        self.setStyleSheet(style_sh)

        self.original_style = style_sh
        self.selected_style = "background-color:#fce3a1;"
        self.hover_style = "background-color:#fef3d7;"

        # self.setContentsMargins(30,0,0,0)

        self.setMaximumHeight(50)
        self.setMinimumHeight(40)

        layout = QHBoxLayout(self.outer_wg)

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(2)

        a = QLabel(str(data["cable_id"])  if data["cable_id"] != None else "-")
        a.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        a.setProperty("class", "outer_left")

        b = QLabel(str(data["cable_code"]) if data["cable_code"] != None else "-")
        b.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        c = QLabel(str(data["line_to_neutral_voltage_level"]) + " V " if data["line_to_neutral_voltage_level"] != None else "-")
        c.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        d = QLabel(str(data["line_to_line_voltage_level"]) + " V " if data["line_to_line_voltage_level"] != None else "-")
        d.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        

        print(data)

        f = QLabel(str(data["current_capacity"]) + " A" if data["current_capacity"] != None else "-")
        f.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        f.setProperty("class", "outer_right")

        layout.addWidget(a)
        layout.addWidget(b)
        layout.addWidget(c)

        layout.addWidget(d)
        layout.addWidget(f)

        self.setLayout(layout)

        self.mousePressEvent = lambda event: self.selected(self.id)
    

    def selection_changed(self, index):
        if self.id == index:
            self.setStyleSheet(self.selected_style)
            self.is_selected = True
            self.user_data["cable_selection"]["cable_id"] = index
            
        else:
            self.setStyleSheet(self.original_style)
            self.is_selected = False


    def selected(self, index):
        self.sig.emit(index)


    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style)
        self.setCursor(QCursor(Qt.PointingHandCursor))


    def leaveEvent(self, event):
        self.setCursor(self.original_cursor)
        if self.is_selected:
            self.setStyleSheet(self.selected_style)
        else:
            self.setStyleSheet(self.original_style)