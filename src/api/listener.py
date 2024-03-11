import socket
import threading
import ast

from config import PORT

class Listener:

    responseBytes : bytes 

    def init(self):
        self.responseBytes = None
        self.startListener()

    def getRecivedBytes(self):
        return self.responseBytes

    def startListener(self):
        
        thread = threading.Thread(target=self.listenerLoop, daemon=True)
        thread.start()
        
    def listenerLoop(self):
            
        sock = socket.socket()
        sock.bind(('', int(5000)))

        while True:
            sock.listen(1)
            conn, addr = sock.accept()

            responseBytes : list[bytes] = []

            tempBytes  = conn.recv(230)
            while tempBytes:
                responseBytes.append(tempBytes)
                tempBytes = conn.recv(230)
            
            # Send HTTP response
            http_response = 'HTTP/1.1 200 OK\n\n'
            conn.sendall(http_response.encode())
            conn.close()


            response = b''.join(responseBytes)
            header_end = response.find(b'\r\n\r\n')
            body = response[header_end+4:]

            self.responseBytes = body
            
            
            print(f"Recived {self.responseBytes.len()} bytes from {addr}")