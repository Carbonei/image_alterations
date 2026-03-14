import zmq 
import time
from PIL import Image
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:8888")
"""
socket.send_string("recolor")
time.sleep(0.3)
socket.recv()
socket.send_string("oni.jpg")
file_path= socket.recv()
img = Image.open(file_path, mode = 'r')

img.show()

"""
"""
socket.send_string("rotate")
time.sleep(0.3)
socket.recv()

socket.send_string("oni.jpg")
socket.recv()

socket.send_string("90")
file_path= socket.recv()


img = Image.open(file_path, mode = 'r')

img.show()

"""

socket.send_string("resize")
time.sleep(0.3)
socket.recv()

socket.send_string("./images/griffin.jpg")
socket.recv()

socket.send_string("90")
socket.recv()

socket.send_string("90")
file_path= socket.recv()

img = Image.open(file_path, mode = 'r')

img.show()
socket.send_string("Q")