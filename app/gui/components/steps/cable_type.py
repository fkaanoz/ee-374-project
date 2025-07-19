from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
   )

from PySide6.QtCore import Qt, Signal

from gui.components.inputs.env_temp import EnvTemperature
from gui.components.inputs.cable_type_spec import CableTypeSpec
from gui.components.inputs.placement_spec import PlacementSpec

from gui.components.toaster.show_toaster import show_msg

class CableType(QWidget):
    input_changed = Signal(int)
    
    def __init__(self, sig, user_input, footer, cable_type_changed=None):
        super().__init__()

        self.calc_sig = sig
        self.user_input = user_input
        self.footer = footer
        self.cable_type_changed = cable_type_changed

        cable_type = QWidget()
        outer_layout = QHBoxLayout(cable_type)

        shp = QWidget()
        shp.setMinimumWidth(700)
        layout = QVBoxLayout(shp)
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0) 
        layout.setAlignment(Qt.AlignCenter | Qt.AlignCenter) 

        self.temp = EnvTemperature(input_changed = self.input_changed)
        self.cable_type_spec = CableTypeSpec(input_changed = self.input_changed, cable_type_changed = self.cable_type_changed)

        self.cable_type_spec.cable_type_changed.connect(self.on_cable_type_changed)
        
        self.placement_spec = PlacementSpec(input_changed = self.input_changed)
        self.placement_spec.setMinimumHeight(35)

        self.empty_box = QWidget()
        self.empty_box.setMinimumHeight(35)
        self.empty_box.hide()

        self.placement_spec.show()

        layout.addWidget(self.temp)
        layout.addWidget(self.cable_type_spec)
        layout.addWidget(self.empty_box)
        layout.addWidget(self.placement_spec)

        outer_layout.addStretch()
        outer_layout.addWidget(shp)
        outer_layout.addStretch()

        self.setLayout(outer_layout)

        self.input_changed.connect(self.get_input)

        
    def on_cable_type_changed(self, selected_id):
        # self.cable_type_changed.emit(selected_id)
        if selected_id == 2:
            self.hide_placement()
        else:
            self.show_placement()


    def show_placement(self):
        self.empty_box.hide()
        self.placement_spec.show()
        

    def hide_placement(self):
        self.empty_box.show()
        self.placement_spec.hide()


    def smart_listing(self, e):
        show_msg("List updated according to input !", self.footer, "SUCCESS")

    def get_input(self):
        temp = self.temp.temp_i.inp.value()
        cable_type_id = self.cable_type_spec.button_group.checkedId()
        placement_id = self.placement_spec.button_group.checkedId()

        cable_type = "Single Core" if cable_type_id == 1 else "Three Core"
        placement = "Flat" if placement_id == 1 else "Trefoil"

        self.user_input["type_env"] = {
                "env_temp" : temp,
                "cable_type": cable_type,
                "placement" : placement
        }

