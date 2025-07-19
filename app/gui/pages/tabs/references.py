from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,

   )


# from gui.style.load_stylesheet import load_stylesheet

class References(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 20, 0, 0) 

        book = QLabel("Fitzpatrick, Martin. Create GUI Applications with Python & Qt6 (PySide6 Edition): The Hands-on Guide to Making Apps with Python. Independently published, 2021.")
        book.setStyleSheet("padding-top:20px;")
        book_det = QLabel("Signaling, Layout and Tabbing ideas taken from that book.")
        book_det.setStyleSheet("font-size: 12px; color: gray;")

        doc_site = QLabel("Qt for Python Documentation. The Qt Company Ltd., 2025, Accessed 23 May 2025 https://doc.qt.io/qtforpython-6/.")
        doc_site.setStyleSheet("padding-top:20px;")
        doc_site_det = QLabel("Usage of lots of Qt widgets and functions mimicked from the documentation.")
        doc_site_det.setStyleSheet("font-size: 12px; color: gray;")
       
        web_site = QLabel("Fitzpatrick, Martin. PySide6 Tutorial 2025: Create Python GUIs with Qt. Python GUIs, Accessed 23 May 2025, https://www.pythonguis.com/pyside6-tutorial/.")
        web_site.setStyleSheet("padding-top:20px;")
        web_site_det = QLabel("Supplementary ideas taken from the tutorials at that site.")
        web_site_det.setStyleSheet("font-size: 12px; color: gray;")
        
        layout.addWidget(book)
        layout.addWidget(book_det)
        layout.addWidget(doc_site)
        layout.addWidget(doc_site_det)
        layout.addWidget(web_site)
        layout.addWidget(web_site_det)
        layout.addStretch()

        self.setLayout(layout)