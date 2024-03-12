from PyQt6.QtGui import QCloseEvent, QPixmap , QImage
from PyQt6.QtWidgets import QWidget, QLabel , QVBoxLayout , QHBoxLayout
from PyQt6.QtCore import Qt

from src.provider.provider import LISTENER_PROVIDER

class ImageViewer(QWidget):

    imageViewerWidth: int
    imageViewerHeight: int
    imageBytes: bytes

    label : QLabel

    def __init__(self ,  imageViewerWidth: int , imageViewerHeight: int , dw : int , dh:int):
        super().__init__()

        self.imageViewerWidth = imageViewerWidth
        self.imageViewerHeight = imageViewerHeight
       
        self.setGeometry(dw, dh, self.imageViewerWidth, self.imageViewerHeight)
        self.setWindowTitle("Recived Image")
        
        self.updateUi()
        
        LISTENER_PROVIDER.subscribeToByteRecive(self.updateUi)

    def closeEvent(self, event: QCloseEvent | None) -> None:
        LISTENER_PROVIDER.onByteResive = None
        return super().closeEvent(event)

  
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
        self.label = QLabel(self)
        self.label.setText("No image recived or error while reciving")

        layout = QHBoxLayout()

        layout.addWidget(self.label , alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)


    def showRecivedImage(self): 
        
        image = QImage.fromData(self.imageBytes)
        pixmap = QPixmap.fromImage(image)

        self.label.setPixmap(pixmap.scaled(self.imageViewerWidth, self.imageViewerHeight, Qt.AspectRatioMode.KeepAspectRatio))
    
        self.label.show()