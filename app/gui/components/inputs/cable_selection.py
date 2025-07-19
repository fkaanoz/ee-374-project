from PySide6.QtWidgets import (    
    QWidget,
    QScrollArea,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QApplication
)

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap


from gui.components.inputs.label import Label
from gui.components.cable_select_line import CableSelectLine
from gui.components.cable_select_header import CableSelectHeader
from gui.style.load_stylesheet import load_stylesheet

from backend.bussiness.calculate import Find_Proper_Cables

class CableSelectionInp(QWidget):
    selected_ = Signal(int)

    def __init__(self, user_input):
        super().__init__()

        self.user_input = user_input

        style_sh = load_stylesheet("cable_selection_inp.css")
        self.setStyleSheet(style_sh)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 10, 0, 0)
        self.layout.setSpacing(0)

        self.curr_screen_width = QApplication.primaryScreen().geometry().width()
        
        self.label_layout = QVBoxLayout()
        self.label_layout.setContentsMargins(0, 6, 0, 3)
        self.label_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


        self.err_message = Label(label="According to your input, there is no proper cable!")
        self.err_message.setMaximumWidth(self.curr_screen_width * 0.84)
        self.err_message.setMinimumHeight(50)
        self.err_message.setStyleSheet("padding-top: 50px; font-size:15px; font-weight:500;")

        self.err_img = QLabel()
        self.pixmap = QPixmap("cross.png")
        self.pixmap = self.pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.err_img.setPixmap(self.pixmap)
        self.err_img.setStyleSheet("padding-top:40px;")



        self.err_message.hide() 

        self.err_img_layout = QHBoxLayout()
        self.err_img_layout.setAlignment(Qt.AlignCenter)
        self.err_img_layout.addWidget(self.err_img)
        
        self.err_img.hide()

        # self.label_layout.addWidget(self.label)
        self.label_layout.addWidget(self.err_message)
        self.label_layout.addLayout(self.err_img_layout)

        self.layout.addLayout(self.label_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QScrollArea.NoFrame)
        self.scroll_area.setAlignment(Qt.AlignCenter)
        
        self.cont_widget = QWidget()
        self.cont_widget.setProperty("class", "cont_widget")
        self.cont_widget.setMaximumWidth(self.curr_screen_width * 0.95)

        self.cont_layout = QVBoxLayout(self.cont_widget)
        self.cont_layout.setSpacing(0)
        self.cont_layout.setContentsMargins(0, 0, 0, 0)

        
        self.lines_container = QWidget()  
        self.lines_layout = QVBoxLayout(self.lines_container)
        self.lines_layout.setSpacing(4)

        self.cont_layout.addWidget(self.lines_container)  
        self.cont_layout.addStretch()
        
        self.scroll_area.setWidget(self.cont_widget)
        self.layout.addWidget(self.scroll_area)

        self.update_list()

        self.selected_.emit(-1)

    def clear_selection(self):
        self.selected_.emit(-1)
        self.user_input["cable_selection"]["cable_id"] = None

    def clear_list(self):
        while self.lines_layout.count():
            item = self.lines_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def update_list(self):
        self.clear_list()

        results = Find_Proper_Cables(self.user_input)

        if len(results) == 0:
            # self.label.hide()
            self.err_message.show()
            self.err_img.show()
        else:
            # self.label.show()
            self.err_message.hide()
            self.err_img.hide()


            # Cable Selection Header
            header = CableSelectHeader()
            self.lines_layout.addWidget(header)
            for _, data in enumerate(results):

                curr_cap = "-"

                if self.user_input["type_env"]["cable_type"] == "Single Core" and self.user_input["type_env"]["placement"] == "Flat":
                    curr_cap = data[4]
                else:
                    curr_cap = data[5]

                line = CableSelectLine(int(data[0]), data={
                    "cable_id": int(data[0]),
                    "cable_code": data[1],
                    "line_to_neutral_voltage_level": data[2],
                    "line_to_line_voltage_level": data[3],
                    "current_capacity": curr_cap,
                }, sig=self.selected_, user_data=self.user_input)

                self.selected_.connect(line.selection_changed)
                self.lines_layout.addWidget(line)