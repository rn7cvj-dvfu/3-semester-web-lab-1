
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit , QLabel  ,QHBoxLayout , QVBoxLayout
from PyQt6.QtWidgets import QFileDialog

from src.app.image_viewer import ImageViewer
from src.utils.converter import Converter
from src.api.sender import Sender

from src.provider.provider import SENDER_PROVIDER

class App(QWidget):

    startButton: QPushButton
    showRecivedDataButton: QPushButton

    ipFieldLabel: QLabel
    ipTextField: QLineEdit

    imageViewer: ImageViewer
    imageViewerWidth: int
    imageViewerHeight: int

    appWidth: int
    appHeight: int

    def __init__(self , appWidth: int , appHeight: int , imageViewerWidth: int , imageViewerHeight: int):
        super().__init__()
        self.appHeight = appHeight
        self.appWidth = appWidth

        self.imageViewerWidth = imageViewerWidth
        self.imageViewerHeight = imageViewerHeight
        
        self.initUI()

    def initUI(self):

        self.setGeometry(200, 200, self.appWidth, self.appHeight)
        self.setWindowTitle("App")

        # Ip enter text field
        self.ipFieldLabel = QLabel(text="Enter IP Address")
        self.ipTextField = QLineEdit()

        ipEnterBox = QHBoxLayout()
        ipEnterBox.addWidget(self.ipFieldLabel)
        ipEnterBox.addWidget(self.ipTextField)

        ipEnterWidget = QWidget()
        ipEnterWidget.setLayout(ipEnterBox)

        # Buttons
        buttonBox = QHBoxLayout()
        self.startButton = QPushButton("Send data")
        self.startButton.clicked.connect(self.sendData)

        self.showRecivedDataButton = QPushButton("Show recived data")
        self.showRecivedDataButton.clicked.connect(self.showRecivedData)

        buttonBox.addWidget(self.startButton)
        buttonBox.addWidget(self.showRecivedDataButton)

        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonBox)

        layout = QVBoxLayout()

        layout.addWidget(ipEnterWidget)
        layout.addWidget(buttonWidget)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setLayout(layout)

    def sendData(self):
        
        dialog = QFileDialog()
        filename, _ = dialog.getOpenFileName(filter="Images (*.jpg)")
        
        ip : str = self.ipTextField.text()
        
        sender : Sender = SENDER_PROVIDER
        sender.sendImage(ip ,filename)

    def showRecivedData(self):
        
    
        self.imageViewer = ImageViewer(self.imageViewerWidth , self.imageViewerHeight)

        self.imageViewer.show()
           
