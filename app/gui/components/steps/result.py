from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QScrollArea
   )

from PySide6.QtCore import Qt

from gui.components.result.selected_cable_info import SelectedCableInfo
from gui.components.result.voltage_regulation_info import VoltageRegulationInfo
from gui.components.result.economic_analysis_info import EconomicAnalysisInfo
from gui.components.result.line_losses_info import LineLossesInfo
from backend.bussiness.calculate import Which_Model

class Result(QWidget):
    def __init__(self, user_input, done_signal):
        super().__init__()

        self.user_input = user_input
        self.done_signal = done_signal

        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignTop)


        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QScrollArea.NoFrame)
        self.scroll_area.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        
        self.content_widget = QWidget()
        self.scroll_area.setWidget(self.content_widget)

        
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignTop)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(10)

        self.choise = SelectedCableInfo(user_input=self.user_input, done_signal=self.done_signal)
        self.content_layout.addWidget(self.choise)

        self.model_layout = QHBoxLayout()
        self.model_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.model_layout.setContentsMargins(30, 10, 0, 0)
        self.model_layout.setSpacing(0)

        self.model_name = Which_Model(self.user_input)
        self.model_explanation = QLabel("Preliminary Note: Model used for ACTIVE POWER calculation below is")
        self.model_label = QLabel(self.model_name)

        self.model_explanation.setStyleSheet("font-size: 14px; padding-left: 10px; background-color: #f0e0e0;")
        self.model_label.setStyleSheet("font-size: 14px; padding: 5px; padding-left:1px; font-weight: bold; background-color: #f0e0e0;")

        self.model_layout.addWidget(self.model_explanation)
        self.model_layout.addWidget(self.model_label)
        self.content_layout.addLayout(self.model_layout)


        self.line_losses = LineLossesInfo(user_input=self.user_input, done_signal=self.done_signal)
        self.voltage_reg = VoltageRegulationInfo(user_input=self.user_input, done_signal=self.done_signal)
        self.econ_analysis = EconomicAnalysisInfo(user_input=self.user_input, done_signal=self.done_signal)

        self.content_layout.addWidget(self.line_losses)
        self.content_layout.addWidget(self.voltage_reg)
        self.content_layout.addWidget(self.econ_analysis)

    
        main_layout.addWidget(self.scroll_area)
        
        self.done_signal.connect(self.update_info)

    def update_info(self):
        self.model_name = Which_Model(self.user_input)
        self.model_label.setText(self.model_name)
