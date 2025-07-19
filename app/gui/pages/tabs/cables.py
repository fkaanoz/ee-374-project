from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QScrollArea,
   )

from gui.components.cable_line import CableLine
from gui.components.table_header import TableHeader
from backend.database.queries import Get_All_Cables



class CablesPage(QWidget):
    def __init__(self):
        super().__init__()

        table_header = TableHeader()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  
        scroll_area.setFrameShape(QScrollArea.NoFrame)

        cont_widget = QWidget()
        cont_layout = QVBoxLayout(cont_widget)

    
        # make request to controller, then add lines!!
        rows = Get_All_Cables()

        for index, r in enumerate(rows):
            a = CableLine(data=r)
            cont_layout.addWidget(a)

        scroll_area.setWidget(cont_widget)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.addWidget(table_header)
        layout.addWidget(scroll_area)

        self.setLayout(layout)