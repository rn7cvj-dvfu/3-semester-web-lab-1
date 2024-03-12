from PyQt6.QtGui import QCloseEvent, QPixmap , QImage
from PyQt6.QtWidgets import QWidget, QLabel , QVBoxLayout , QHBoxLayout
from PyQt6.QtCore import Qt

from src.provider.provider import LISTENER_PROVIDER

class ImageViewer(QWidget):

    imageViewerWidth: int
    imageViewerHeight: int
    imageBytes: bytes
    imageLabel : QLabel

    def __init__(self ,  imageViewerWidth: int , imageViewerHeight: int):
        super().__init__()

        self.imageViewerWidth = imageViewerWidth
        self.imageViewerHeight = imageViewerHeight
       
        # LISTENER_PROVIDER.subscribeToByteRecive(self.updateUi)

        self.setGeometry(200, 200, self.imageViewerWidth, self.imageViewerHeight)
      
        self.setWindowTitle("Recived Image")

        self.updateUi()

    def updateUi(self):
        self.imageBytes = LISTENER_PROVIDER.getRecivedBytes()
        
        if not self.imageBytes:
            print("Invalid image")
            self.showError()
            return
            
        try:
            self.showRecivedImage()
            print("Update image")
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

        self.imageLabel = QLabel(self)
        self.imageLabel.setPixmap(pixmap.scaled(self.imageViewerWidth, self.imageViewerHeight, Qt.AspectRatioMode.KeepAspectRatio))

        self.imageLabel.move(0, 0 )

        self.imageLabel.show()