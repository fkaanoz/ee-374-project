from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)
from decimal import Decimal

from PySide6.QtWidgets import QSizePolicy 
from PySide6.QtCore import Signal

from gui.components.progress_labels import ProgressLabel
from gui.style.load_stylesheet import load_stylesheet

from gui.components.toaster.show_toaster import show_msg

from gui.constants.user_data_base import ClearUserData

class Progress(QWidget):
    stepChanged = Signal(int) 

    def __init__(self, last_step, calc_sig, user_data, footer, reset_sig, done_signal):
        super().__init__()
        self.done_signal = done_signal # used for signal when the calculation is done !

        self.current_step = 0
        self.last_step = last_step

        self.calc_sig = calc_sig
        self.user_data = user_data

        self.footer = footer

        self.reset_sig = reset_sig

        style_sh = load_stylesheet("progress.css")
        self.setStyleSheet(style_sh)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 7, 0, 0) 
        layout.setSpacing(0)


        self.load_spec = ProgressLabel(step="1. Load Specification", index=0)
        self.sep0 = QLabel(">>")
        self.cable_type = ProgressLabel(step="2. Cable Type & Environment", index=1)
        self.sep1 = QLabel(">>")
        self.cable_selection = ProgressLabel(step="3. Cable Selection", index=2)
        self.sep2 = QLabel(">>")
        self.cable_length = ProgressLabel(step="4. Cable Length & Parallel Circuit", index=3)
        self.sep3 = QLabel(">>")
        self.result = ProgressLabel(step="5. Result", index=4)


        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.load_spec.setSizePolicy(size_policy)
        self.cable_type.setSizePolicy(size_policy)
        self.cable_selection.setSizePolicy(size_policy)
        self.result.setSizePolicy(size_policy)


        layout.addWidget(self.load_spec)
        layout.addWidget(self.sep0)
        layout.addWidget(self.cable_type)
        layout.addWidget(self.sep1)
        layout.addWidget(self.cable_selection)
        layout.addWidget(self.sep2)
        layout.addWidget(self.cable_length)
        layout.addWidget(self.sep3)
        layout.addWidget(self.result)
        layout.addStretch()             

        self.setLayout(layout)

        self.stepChanged.connect(self.load_spec.step_changed)
        self.stepChanged.connect(self.cable_type.step_changed)
        self.stepChanged.connect(self.cable_selection.step_changed)
        self.stepChanged.connect(self.cable_length.step_changed)
        self.stepChanged.connect(self.result.step_changed)

    def nextStepHandler(self):
        # input check logic!
        # print("user data: ", self.user_data)
        match self.current_step:
            case 0:
                if CheckLoadSpec(self.user_data):
                    self.current_step = self.current_step + 1
                    self.stepChanged.emit(self.current_step)
                else:
                    show_msg(msg="WARN: Active Power or Rated Voltage Fields is 0.00 !  Please fill all the required fields! ", parent=self.footer, type="WARN")
            case 1:
                if CheckTypeSpec(self.user_data):
                    self.current_step = self.current_step + 1
                    self.stepChanged.emit(self.current_step)
                else:
                    show_msg(msg="Please fill all the required fields! ", parent=self.footer, type="WARN")

            case 2:
                if CheckSelection(self.user_data):
                    self.current_step = self.current_step + 1
                    self.stepChanged.emit(self.current_step)
                else:
                    show_msg(msg="Please select one of the cable above! ", parent=self.footer, type="WARN")
            case 3:
                
                if CheckLength(self.user_data):
                    self.current_step = self.current_step + 1
                    self.stepChanged.emit(self.current_step)
                    self.done_signal.emit()
                    
                else:
                    show_msg(msg="Please fill all the required fields! ", parent=self.footer, type="WARN")


    def prevStepHandler(self):
        if(self.current_step > 0):
            self.current_step = self.current_step - 1
            self.stepChanged.emit(self.current_step)

    def clearHandler(self):
        self.reset_sig.emit()
        

    def initCalculatorStep(self):
        self.stepChanged.emit(0)

def CheckLoadSpec(user_data):
    v = user_data["load_spec"]["rated_voltage"]
    a_p = user_data["load_spec"]["active_power"]
    r_p = user_data["load_spec"]["reactive_power"]
    try:
        voltage = Decimal(v)
        active_power = Decimal(a_p)
        reactive_power = Decimal(r_p)
        if voltage == Decimal("0.0") or active_power == Decimal("0.0") or reactive_power == None:
            return False
        return True
    except:
        if v == None or a_p == None:
            return False
        return True
    

def CheckTypeSpec(user_data):
    return True

def CheckSelection(user_data):
    if user_data["cable_selection"]["cable_id"] == None:
        return False
    return True

def CheckLength(user_data):
    if user_data["cable_length"]["length"] == None or user_data["cable_length"]["length"] == 0:
        return False

    if user_data["cable_length"]["number_of_parallel_circuits"] == None or user_data["cable_length"]["number_of_parallel_circuits"] == 0:
        return False

    return True