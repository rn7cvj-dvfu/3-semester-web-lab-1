import os
import httpx
import socket

from config import PORT

from src.utils.converter import Converter

class Sender:

    converter : Converter

    def __init__(self , converter : Converter):
        self.converter = converter

    def sendImage(self, host:str , path: str):

        imageBytes = None

        print(f"Sending image to {host}")
        print(f"Image path: {path}")
    
        try:
            os.stat(path)
            imageBytes : bytes = self.converter.imgToBytes(path)
        except Exception as ex:
            print(f'Erro while parsing image: {ex}')
            return
     

        try:
            headers = {'Content-Type': 'application/octet-stream'}
            req = httpx.post(f"http://{host}:{PORT}", data=imageBytes , headers=headers )    
            print(req.status_code)
        except Exception as ex:
            return