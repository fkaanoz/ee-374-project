from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
   )

from PySide6.QtCore import Qt, Signal

from gui.components.progress import Progress

from gui.components.next_step_button import NextStep
from gui.components.prev_step_button import PreviousStep
from gui.components.clear_button import ClearButton

from gui.components.steps.load_spec import LoadSpec
from gui.components.steps.cable_type import CableType
from gui.components.steps.cable_select import CableSelect
from gui.components.steps.cable_length import CableLength
from gui.components.steps.result import Result

from gui.constants.user_data_base import ClearUserData


class Calculator(QWidget):
    calc_sig = Signal(int)
    reset_sig = Signal()
    cable_type_changed_sig = Signal(int)
    done_signal = Signal()

    def __init__(self, footer):
        super().__init__()

        self.footer = footer

        self.user_input = ClearUserData()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0)

        body = QWidget()
        self.steps = Progress(last_step=5, calc_sig=self.calc_sig, user_data=self.user_input, footer=self.footer, reset_sig=self.reset_sig, done_signal=self.done_signal)

        bodyLayout = QVBoxLayout(body)
        bodyLayout.setContentsMargins(0, 0, 0, 0) 
        bodyLayout.setAlignment(Qt.AlignTop)
        bodyLayout.addWidget(self.steps)


        self.tab_widget = QTabWidget()
        self.tab_widget.tabBar().setVisible(False)  

        self.load_spec_tab = LoadSpec(sig=self.calc_sig, user_input=self.user_input)
        self.cable_type_tab = CableType(sig=self.calc_sig, user_input=self.user_input, footer=self.footer, cable_type_changed=self.cable_type_changed_sig)
        self.cable_select_tab = CableSelect(sig=self.calc_sig, user_input=self.user_input)
        self.cable_length = CableLength(sig=self.calc_sig, user_input=self.user_input, footer=self.footer, cable_type_changed=self.cable_type_changed_sig)
        self.result = Result(user_input=self.user_input, done_signal=self.done_signal)

        self.tab_widget.addTab(self.load_spec_tab, "")
        self.tab_widget.addTab(self.cable_type_tab, "")
        self.tab_widget.addTab(self.cable_select_tab, "")
        self.tab_widget.addTab(self.cable_length, "")
        self.tab_widget.addTab(self.result, "")

        self.steps.stepChanged.connect(self.tab_widget.setCurrentIndex)
        
        
        self.calc_sig.connect(self.cable_type_tab.smart_listing)
        self.calc_sig.connect(self.cable_select_tab.clear_selection)
        self.calc_sig.connect(self.cable_select_tab.cable_sel.update_list)

        self.steps.stepChanged.connect(self.connect_signals)

        bodyLayout.addWidget(self.tab_widget)
    
        ns = NextStep(handler=self.steps.nextStepHandler)
        ps = PreviousStep(handler=self.steps.prevStepHandler)
        cl = ClearButton(handler=self.steps.clearHandler)

        btLayout = QHBoxLayout()
        btLayout.addWidget(cl)
        btLayout.addStretch()
        btLayout.addWidget(ps)
        btLayout.addWidget(ns)
        btLayout.setAlignment(Qt.AlignRight)

        layout.addWidget(body,1)
        layout.addLayout(btLayout)

        self.setLayout(layout)

        self.steps.initCalculatorStep()
        

    def connect_signals(self, e):
        if e == 2:
            self.calc_sig.emit(e)

    