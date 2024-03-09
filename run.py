from PyQt6.QtWidgets import QApplication
import sys

from src.app.app import App

from config import WINDOW_WIDTH, WINDOW_HEIGHT , IMAGE_VIEWER_WIDTH , IMAGE_VIEWER_HEIGHT

if __name__ == '__main__':


    qApp = QApplication(sys.argv)
    app : App = App(WINDOW_WIDTH , WINDOW_HEIGHT, IMAGE_VIEWER_WIDTH , IMAGE_VIEWER_HEIGHT)
    app.show()
    
    sys.exit(qApp.exec())