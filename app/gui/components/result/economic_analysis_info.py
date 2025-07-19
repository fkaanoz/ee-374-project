from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
   )

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy

from gui.style.load_stylesheet import load_stylesheet
from gui.components.result.cost_table import CostTable


class EconomicAnalysisInfo(QWidget):
    def __init__(self, user_input, done_signal):
        super().__init__()

        style_sh = load_stylesheet("economic_analysis.css")
        self.setStyleSheet(style_sh)

        self.user_input = user_input
        self.done_signal = done_signal

        layout = QVBoxLayout(self)
        
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.setSpacing(0)

        label = QLabel("4. Economic Analysis of Your Choice *: ")
        label.setStyleSheet("font-size: 15px; font-weight: bold; padding: 5px; padding-left: 10px;")
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setContentsMargins(0, 0, 0, 0)
        
        layout.addWidget(label)

        cost_table = CostTable(self.user_input, self.done_signal)

        layout.addWidget(cost_table)

        # notes
        l1 = QLabel("* The economic analysis is based on the following assumptions:")
        l1.setStyleSheet("font-size: 12px; padding: 5px; padding-left: 10px;")
        l1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        l1.setContentsMargins(20, 10, 0, 0)
        layout.addWidget(l1)
        assm_layout = QVBoxLayout()
        assm_layout.setContentsMargins(30,0,0,0)
        assm_layout.setSpacing(0)
        assm1 = QLabel("1) Electricity price: 2500 TL/MWh")
        assm1.setStyleSheet("font-size: 11px; padding-left: 10px;")
        assm2 = QLabel("2) Industrial Load Usage : 10 h/day")
        assm2.setStyleSheet("font-size: 11px; padding-left: 10px;")
        assm3 = QLabel("3) Residential Load Usage : 5 h/day")
        assm3.setStyleSheet("font-size: 11px; padding-left: 10px;")
        assm4 = QLabel("4) Municipal Load Usage : 12 h/day")
        assm4.setStyleSheet("font-size: 11px; padding-left: 10px;")
        assm5 = QLabel("5) Commercial Load Usage : 8 h/day")
        assm5.setStyleSheet("font-size: 11px; padding-left: 10px;")
        assm6 = QLabel("6) Operation last 10 years")
        assm6.setStyleSheet("font-size: 11px; padding-left: 10px;")

        assm_layout.addWidget(assm1)
        assm_layout.addWidget(assm2)
        assm_layout.addWidget(assm3)
        assm_layout.addWidget(assm4)
        assm_layout.addWidget(assm5)
        assm_layout.addWidget(assm6)

        layout.addLayout(assm_layout)

        # self.done_signal.connect(self.update_info)

    # def update_info(self):
        # print("update_info at EconomicAnalysisInfo")