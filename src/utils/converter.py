import os
import numpy as np

class Converter:

  def imgToBytes(self, path: str) -> bytes:

    with open(path, 'rb') as f:
        bytes_data = f.read()

    int_array = np.frombuffer(bytes_data, dtype=np.uint8)

    # file = str(list(int_array))[1:-1]
    
    return int_array.tobytes()


  def bytesToImg(self, file: str, name: str):
      
      try:

          byte_arr = list(map(lambda x: int(x), file.split(",")))
          some_bytes = bytearray(byte_arr)

          immutable_bytes = bytes(some_bytes)

          with open(f"{STATIC_PATH}/{name}.jpg", "wb") as f:
              f.write(immutable_bytes)
          
          f.close()
          
      except Exception as e:
          print(e)