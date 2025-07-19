from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QFont


from gui.style.load_stylesheet import load_stylesheet
from gui.components.tabs.cables_label import CablesLabel
from gui.components.tabs.references_label import ReferencesLabel
from gui.components.tabs.main_label import MainPageLabel


class Header(QWidget):
    tabChanged = Signal(int) 

    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout(self)
        
        self.header = QWidget()

        self.title = QLabel("ee-374-group-7")

        self.main_page = MainPageLabel(index=0)
        self.cables_page = CablesLabel(index=1)
        self.references = ReferencesLabel(index=2)

        self.main_page_original_font = self.main_page.font()

        self.title.setProperty("class","titleLabel")      
        self.main_page.setProperty("class","mainPageLabel")      
        self.cables_page.setProperty("class","cablesPageLabel")      
        self.references.setProperty("class","referencesPageLabel")      

        
        header_layout = QHBoxLayout(self.header)
        header_layout.addWidget(self.title)
        header_layout.addStretch()
        header_layout.addWidget(self.main_page)
        header_layout.addWidget(self.cables_page)
        header_layout.addWidget(self.references)

        style_sh = load_stylesheet("header.css")
        self.header.setStyleSheet(style_sh)
    
        self.header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.header)

        self.main_page.mousePressEvent = lambda event: self.tabClicked(0)
        self.cables_page.mousePressEvent = lambda event: self.tabClicked(1)
        self.references.mousePressEvent = lambda event: self.tabClicked(2)
    
    
        self.tabChanged.connect(self.main_page.tab_changed)
        self.tabChanged.connect(self.cables_page.tab_changed)
        self.tabChanged.connect(self.references.tab_changed)

        self.tabClicked(0)          # initial page

    def tabClicked(self, index):
        self.tabChanged.emit(index)