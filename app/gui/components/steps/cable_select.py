from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
   )

from PySide6.QtCore import Qt, Signal

from gui.components.inputs.cable_selection import CableSelectionInp

class CableSelect(QWidget):
    input_changed = Signal(int)
    
    def __init__(self, sig, user_input):
        super().__init__()

        self.calc_sig = sig
        self.user_input = user_input

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0) 
        layout.setAlignment(Qt.AlignLeft | Qt.AlignTop) 

        self.cable_sel = CableSelectionInp(user_input = self.user_input)
        layout.addWidget(self.cable_sel)

    def clear_selection(self):
        self.cable_sel.clear_selection()
