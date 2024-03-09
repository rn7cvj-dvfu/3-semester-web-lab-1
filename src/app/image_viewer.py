from PyQt6.QtGui import QPixmap , QImage
from PyQt6.QtWidgets import QWidget, QLabel , QVBoxLayout , QHBoxLayout
from PyQt6.QtCore import Qt

from src.provider.provider import LISTENER_PROVIDER

class ImageViewer(QWidget):

    imageViewerWidth: int
    imageViewerHeight: int
    imageBytes: bytes

    def __init__(self ,  imageViewerWidth: int , imageViewerHeight: int):
        super().__init__()

        self.imageViewerWidth = imageViewerWidth
        self.imageViewerHeight = imageViewerHeight
        self.imageBytes = LISTENER_PROVIDER.getRecivedBytes()

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, self.imageViewerWidth, self.imageViewerHeight)
        self.setWindowTitle("Recived Image")
        
        if self.imageBytes:
            try:
                self.showRecivedImage()
                return
            except:
                print("Error showing image")
        
        self.showError()

    def showError(self):
        label = QLabel(self)
        label.setText("No image recived or error while reciving")

        layout = QHBoxLayout()

        layout.addWidget(label , alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def showRecivedImage(self): 
        
        image = QImage.fromData(self.imageBytes)
        pixmap = QPixmap.fromImage(image)
        label = QLabel(self)
        label.setPixmap(pixmap.scaled(self.imageViewerWidth, self.imageViewerHeight, Qt.AspectRatioMode.KeepAspectRatio))
        label.show()
