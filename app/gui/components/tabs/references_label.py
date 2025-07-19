from PySide6.QtWidgets import (    
    QLabel,
)
from PySide6.QtGui import QCursor, Qt

from gui.style.load_stylesheet import load_stylesheet

class ReferencesLabel(QLabel):
    def __init__(self, index):
        super().__init__()

        self.index = index
        self.setText("References")

        self.setProperty("class","referencesPageLabel")         # for CSS

        self.style_sh = load_stylesheet("header.css")
        self.setStyleSheet(self.style_sh)

        self.original_cursor = self.cursor()

        self.setAlignment(Qt.AlignCenter) 


    def enterEvent(self, event):
        self.setCursor(QCursor(Qt.PointingHandCursor))
        

    def leaveEvent(self, event):
        self.setCursor(self.original_cursor)
        

    
    def tab_changed(self, index):
        if index == self.index:
            self.setStyleSheet("background-color: white;")
        else:
            self.setStyleSheet(self.style_sh)
        
        
