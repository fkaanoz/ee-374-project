from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QGridLayout
)

from PySide6.QtCore import Qt

from backend.bussiness.calculate import Calculate_Active_Losses
from backend.bussiness.calculate import Calculate_Reactive_Losses

from gui.style.load_stylesheet import load_stylesheet


class LineLossesInfo(QWidget):
    def __init__(self, user_input, done_signal):
        super().__init__()

        style_sh = load_stylesheet("line_losses.css")
        self.setStyleSheet(style_sh)

        self.user_input = user_input
        self.done_signal = done_signal

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        main_layout.setSpacing(0)

        title_label = QLabel("2. Line Losses: ")
        title_label.setStyleSheet("font-size: 15px; font-weight: bold; padding: 5px; padding-left: 10px;")
        title_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        title_label.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(title_label)

        
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(10, 0, 0, 0)
        grid_layout.setHorizontalSpacing(40)
        grid_layout.setVerticalSpacing(2)

        grid_layout.setColumnStretch(0, 2)
        grid_layout.setColumnStretch(1, 2)

    
        active_label = QLabel("Active Losses:")
        active_label.setStyleSheet("font-size: 15px; padding: 5px; padding-left: 10px; padding-bottom:0px; padding-right: 2px;")
        active_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.active_losses_value_label = QLabel("0.00 MW")
        self.active_losses_value_label.setStyleSheet("font-size: 15px; padding: 5px; padding-left: 10px; font-weight: bold;")
        self.active_losses_value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        active_row_layout = QHBoxLayout()
        active_row_layout.addWidget(active_label)
        active_row_layout.addStretch()
        active_row_layout.addWidget(self.active_losses_value_label)

        active_formula = QLabel("Loss<sub>active</sub> = I<sub>rms</sub><sup>2</sup> * R<sub>total</sub>")
        active_formula.setTextFormat(Qt.RichText)
        active_formula.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        active_formula.setStyleSheet("font-size: 15px; padding-right: 10px;")

        grid_layout.addLayout(active_row_layout, 0, 0)
        grid_layout.addWidget(active_formula, 0, 1)

        reactive_label = QLabel("Reactive Losses:")
        reactive_label.setStyleSheet("font-size: 15px; padding: 5px; padding-left: 10px; padding-right: 2px;")
        reactive_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.reactive_losses_value_label = QLabel("0.00 MVAr")
        self.reactive_losses_value_label.setStyleSheet("font-size: 15px; padding: 5px; padding-left: 10px; font-weight: bold;")
        self.reactive_losses_value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        reactive_row_layout = QHBoxLayout()
        reactive_row_layout.addWidget(reactive_label)
        reactive_row_layout.addStretch()
        reactive_row_layout.addWidget(self.reactive_losses_value_label)

        reactive_formula = QLabel("Loss<sub>reactive</sub> = I<sub>rms</sub><sup>2</sup> * X<sub>total</sub>")
        reactive_formula.setTextFormat(Qt.RichText)
        reactive_formula.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        reactive_formula.setStyleSheet("font-size: 15px; padding-right: 10px;")

        grid_layout.addLayout(reactive_row_layout, 1, 0)
        grid_layout.addWidget(reactive_formula, 1, 1)

        main_layout.addLayout(grid_layout)

        self.done_signal.connect(self.update_info)

    def update_info(self):
        active_losses = Calculate_Active_Losses(self.user_input)
        active_losses = active_losses * 1000
        self.active_losses_value_label.setText(f"{active_losses:.4f} KW")

        reactive_losses = Calculate_Reactive_Losses(self.user_input)
        reactive_losses = reactive_losses * 1000
        self.reactive_losses_value_label.setText(f"{reactive_losses:.4f} KVar")
