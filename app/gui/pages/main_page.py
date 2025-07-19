from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QTabWidget)


from gui.style.load_stylesheet import load_stylesheet
from gui.components.header import Header
from gui.components.footer import Footer

from gui.pages.tabs.cables import CablesPage
from gui.pages.tabs.calculator import Calculator
from gui.pages.tabs.references import References

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        
        style_sh = load_stylesheet("main_page.css")
        self.setStyleSheet(style_sh)

        self.tab_widget = QTabWidget()
        self.tab_widget.tabBar().setVisible(False)  

        self.h = Header()
        self.f = Footer()
        
        self.tab1 = Calculator(footer=self.f)
        self.tab2 = CablesPage()
        self.tab3 = References()

        self.tab1.reset_sig.connect(self.reset_calculator)


        self.tab_widget.addTab(self.tab1, "")
        self.tab_widget.addTab(self.tab2, "")
        self.tab_widget.addTab(self.tab3, "")

        self.h.tabChanged.connect(self.tab_widget.setCurrentIndex)

        layout.addWidget(self.h)
        layout.addWidget(self.tab_widget)
        layout.addWidget(self.f)
        
        self.setLayout(layout)
        self.setWindowTitle("ee-374-group-7")
        self.showMaximized()


    def reset_calculator(self):
        self.tab_widget.removeTab(0)
        self.tab1.deleteLater()

        self.tab1 = Calculator(footer=self.f)
        self.tab1.reset_sig.connect(self.reset_calculator)
        self.tab_widget.insertTab(0, self.tab1, "")
        self.tab_widget.setCurrentIndex(0) 