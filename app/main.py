import sys
import os
from PySide6.QtWidgets import (QApplication)
from PySide6.QtCore import QTimer

from gui.pages.main_page import MainPage
from gui.pages.intro_page import IntroPage

from PySide6.QtGui import QFontDatabase       

if __name__ == '__main__':

    app = QApplication(sys.argv)

    dir = os.path.dirname(os.path.abspath(__file__))
    #tektur_font_path = os.path.join(dir, "gui/style/fonts/tektur/tektur.ttf")
    
    # for windows: 
    tektur_font_path = os.path.join(dir, "gui\\style\\fonts\\tektur\\tektur.ttf")

    tektur_font_id = QFontDatabase.addApplicationFont(tektur_font_path)
    tektur_font_families = QFontDatabase.applicationFontFamilies(tektur_font_id)


    # quicksand_font_path = os.path.join(dir, "gui/style/fonts/quicksand/quicksand.ttf")
    
    # for windows: 
    quicksand_font_path = os.path.join(dir, "gui\\style\\fonts\\quicksand\\quicksand.ttf")

    quicksand_font_id = QFontDatabase.addApplicationFont(quicksand_font_path)
    quicksand_font_families = QFontDatabase.applicationFontFamilies(quicksand_font_id)

    if quicksand_font_id == -1:
        print(f"Failed to load Quicksand font from {quicksand_font_path}")
    else:
        print(f"Quicksand font loaded successfully: {quicksand_font_families}")

    intro_widget = IntroPage()
    main_widget = MainPage()

    main_widget.hide()

    def hide_and_show_main_page():
        intro_widget.closeWithAnimation(on_finished=main_widget.show) 

    intro_widget.show()

    # it will call show_main_page after 2.2 secs
    QTimer.singleShot(2200, hide_and_show_main_page) 

    sys.exit(app.exec())