from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QGridLayout
)

from PySide6.QtCore import Qt

from gui.style.load_stylesheet import load_stylesheet
from backend.bussiness.calculate import Calculate_Voltage_Regulation


class VoltageRegulationInfo(QWidget):
    def __init__(self, user_input, done_signal):
        super().__init__()

        self.user_input = user_input
        self.done_signal = done_signal

        style_sh = load_stylesheet("voltage_regulation.css")
        self.setStyleSheet(style_sh)

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        main_layout.setSpacing(0)

        title_label = QLabel("3. Voltage Regulation: ")
        title_label.setStyleSheet("font-size: 15px; font-weight: bold; padding: 5px; padding-left: 10px;")
        title_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        title_label.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(title_label)

        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(10, 0, 0, 0)
        grid_layout.setHorizontalSpacing(40)
        grid_layout.setVerticalSpacing(10)

        grid_layout.setColumnStretch(0, 2)
        grid_layout.setColumnStretch(1, 2)

        
        voltage_label = QLabel("Voltage Regulation:")
        voltage_label.setStyleSheet("font-size: 15px; padding: 5px; padding-left: 10px; padding-right: 2px;")
        voltage_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.voltage_value_label = QLabel("0.00 %")  # placeholder value
        self.voltage_value_label.setStyleSheet("font-size: 15px; font-weight : bold;")
        self.voltage_value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        voltage_row_layout = QHBoxLayout()
        voltage_row_layout.addWidget(voltage_label)
        voltage_row_layout.addStretch()
        voltage_row_layout.addWidget(self.voltage_value_label)

        voltage_reg_formula = QLabel("Reg = (V<sub>no-load</sub> - V<sub>full-load</sub>) / V<sub>full-load</sub> * 100%")
        voltage_reg_formula.setTextFormat(Qt.RichText)
        voltage_reg_formula.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        voltage_reg_formula.setStyleSheet("font-size: 15px;")

        grid_layout.addLayout(voltage_row_layout, 0, 0)
        grid_layout.addWidget(voltage_reg_formula, 0, 1)

        main_layout.addLayout(grid_layout)

        self.done_signal.connect(self.update_info)

    def update_info(self):
        calculated_voltage_regulation = Calculate_Voltage_Regulation(self.user_input)
        
        self.voltage_value_label.setText(f"{calculated_voltage_regulation:.4f} %")
        
