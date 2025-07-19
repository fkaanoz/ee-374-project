from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout
from PySide6.QtCore import Qt, Signal
from gui.style.load_stylesheet import load_stylesheet
from backend.database.queries import Get_Price_Of_Cable
from backend.bussiness.calculate import Calculate_Active_Losses


class CostTable(QWidget):
    def __init__(self, user_input, done_signal):
        super().__init__()

        style_sh = load_stylesheet("cost_table.css")
        self.setStyleSheet(style_sh)

        self.user_input = user_input
        self.done_signal = done_signal

        layout = QGridLayout()
        layout.setContentsMargins(25, 10, 0, 15)
        layout.setHorizontalSpacing(40)
        layout.setVerticalSpacing(10)
        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)

        # Cable Cost Row
        self.label = QLabel("Cable Cost:")
        self.label.setStyleSheet("font-size: 15px;")

        self.inst_full_calculation = QLabel("")
        self.inst_full_calculation.setStyleSheet("font-weight: bold; font-size:15px;")

        cable_row_layout = QHBoxLayout()
        cable_row_layout.addWidget(self.label, alignment=Qt.AlignLeft)
        cable_row_layout.addStretch()
        cable_row_layout.addWidget(self.inst_full_calculation, alignment=Qt.AlignRight)

        cable_formula = QLabel("Cost<sub>cable</sub> = Length<sub>cable</sub> * Price<sub>km</sub> * N<sub>parallel</sub>")
        cable_formula.setTextFormat(Qt.RichText)

        layout.addLayout(cable_row_layout, 0, 0)
        layout.addWidget(cable_formula, 0, 1, alignment=Qt.AlignRight)

        # Active Losses Cost Row
        self.active_losses_label = QLabel("Active Losses Cost:")
        self.active_losses_label.setStyleSheet("font-size: 15px;")

        self.loss_full_calculation = QLabel("")
        self.loss_full_calculation.setStyleSheet("font-weight: bold; font-size:15px;")

        loss_row_layout = QHBoxLayout()
        loss_row_layout.addWidget(self.active_losses_label, alignment=Qt.AlignLeft)
        loss_row_layout.addStretch()
        loss_row_layout.addWidget(self.loss_full_calculation, alignment=Qt.AlignRight)

        loss_formula = QLabel("Cost<sub>loss</sub> = Loss<sub>active</sub> * Price<sub>MGW</sub> * Hour<sub>yearly</sub> * 10")
        loss_formula.setTextFormat(Qt.RichText)

        layout.addLayout(loss_row_layout, 1, 0)
        layout.addWidget(loss_formula, 1, 1, alignment=Qt.AlignRight)

        # Total Cost Row
        self.total_cost_label = QLabel("Total Cost (Cable + Active Losses):")
        self.total_cost_label.setStyleSheet("font-size: 15px; font-weight: bold;")

        self.total_cost_value_label = QLabel("0.00 TL")
        self.total_cost_value_label.setStyleSheet("font-size: 15px; font-weight: bold;")

        total_row_layout = QHBoxLayout()
        total_row_layout.addWidget(self.total_cost_label, alignment=Qt.AlignLeft)
        total_row_layout.addStretch()
        total_row_layout.addWidget(self.total_cost_value_label, alignment=Qt.AlignRight)

        layout.addLayout(total_row_layout, 2, 0)

        self.setLayout(layout)

        self.done_signal.connect(self.update_info)

    def update_info(self):
        length_of_cable = self.user_input["cable_length"]["length"]
        per_km_price = Get_Price_Of_Cable(self.user_input["cable_selection"]["cable_id"])
        number_of_parallel_circuits = self.user_input["cable_length"]["number_of_parallel_circuits"]
        cost = length_of_cable * per_km_price * number_of_parallel_circuits

        if self.user_input["type_env"]["cable_type"] == "Single Core":
            cost = cost * 3     # if it is single core, make it 3 core from single line cables

        inst_formatted_cost = f"= {cost:,.2f} ₺".replace(",", "X").replace(".", ",").replace("X", ".")
        self.inst_full_calculation.setText(inst_formatted_cost)

        active_power_loss = Calculate_Active_Losses(self.user_input)
        load_type = self.user_input["load_spec"]["load_type"]

        hours_per_day = {
            "Industrial": 10,
            "Residential": 5,
            "Municipal": 12,
            "Commercial": 8
        }.get(load_type, 0)

        days_per_year = 365
        price_per_mwh = 2500
        hours_per_year = hours_per_day * days_per_year

        act_cost = active_power_loss * price_per_mwh * hours_per_year * 10

        act_formatted_cost = f"= {act_cost:,.2f} ₺".replace(",", "X").replace(".", ",").replace("X", ".")
        self.loss_full_calculation.setText(act_formatted_cost)

        total_cost = cost + act_cost
        total_formatted_cost = f"= {total_cost:,.2f} ₺".replace(",", "X").replace(".", ",").replace("X", ".")
        self.total_cost_value_label.setText(total_formatted_cost)
