import socket
import threading
import ast

from config import PORT

class Listener:

    responseBytes : bytes 
    onByteResive : callable

    def __init__(self):
        self.responseBytes = None
        self.onByteResive  = None
        self.startListener()

    def getRecivedBytes(self):
        return self.responseBytes

    def subscribeToByteRecive(self , onByteResive: callable):
        self.onByteResive = onByteResive

    def startListener(self):
        
        thread = threading.Thread(target=self.listenerLoop, daemon=True)
        thread.start()
        
    def listenerLoop(self):
            
        sock = socket.socket()
        sock.bind(('', int(PORT)))

        while True:
            sock.listen(1)
            conn, addr = sock.accept()

            print(f"Connecion from {addr[0]}")

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
            
            
            print(f"Recived {self.responseBytes.__len__()} bytes from {addr[0]}")

            if self.onByteResive:
                self.onByteResive()
                