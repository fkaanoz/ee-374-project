from PySide6.QtWidgets import (    
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,QApplication)
from PySide6.QtCore import Qt
from PySide6.QtCore import QPropertyAnimation, QEasingCurve


from gui.style.load_stylesheet import load_stylesheet


class IntroPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        style_sh = load_stylesheet("intro_page.css")
        self.setStyleSheet(style_sh)

        body = QWidget()
        body_layout = QVBoxLayout(body)

        title = QLabel("ee-374-power-cable-ui")    
        motto= QLabel("fkaanoz")       

        version = QLabel("v1.1.0")

        title.setProperty("class", "titleLabel")
        motto.setProperty("class", "mottoLabel")   
        version.setProperty("class", "versionLabel")   

        body.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        body_layout.addWidget(title)
        body_layout.addWidget(motto)

        title.setAlignment(Qt.AlignBottom | Qt.AlignHCenter) 
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        motto.setAlignment(Qt.AlignTop| Qt.AlignHCenter) 
        version.setAlignment(Qt.AlignTop| Qt.AlignHCenter) 

        layout.addWidget(body)
        layout.addWidget(version)
        
        self.setLayout(layout)
        self.setWindowTitle("ee-374-group-7")

        intro_width = 800
        intro_height = 540
        
        self.setGeometry(300, 300, intro_width, intro_height)       # x,y,  width, heigh

        # then go to middle of the screen.
        screen = QApplication.primaryScreen().geometry()
        mid_x = (screen.width() - intro_width) // 2
        mid_y = (screen.height() - intro_height) // 2
        
        self.move(mid_x, mid_y)  

    def closeWithAnimation(self, on_finished=None):
        def close():
            self.close()
            if on_finished:
                on_finished()

        self.animation = QPropertyAnimation(self, b"windowOpacity") 
        self.animation.setDuration(500)  
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

        self.animation.finished.connect(close)  
        self.animation.start()

