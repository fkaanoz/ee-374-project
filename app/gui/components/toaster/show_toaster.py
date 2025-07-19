from PySide6.QtWidgets import QApplication

from gui.components.toaster.success import SuccessToast
from gui.components.toaster.warn import WarnToast
from gui.components.toaster.error import ErrorToast

def show_msg(msg, parent, type):
    toaster = None

    if type == "SUCCESS":
        toaster = SuccessToast(msg, parent)
    elif type == "WARN":
        toaster = WarnToast(msg, parent)
    else:
        toaster = ErrorToast(msg, parent)

    screen_rect = parent.geometry()
    
    x = screen_rect.left()
    y = screen_rect.bottom() + 20

    toaster.move(x,y)
    # toaster.move(screen_rect.bottomRight())
    toaster.show()