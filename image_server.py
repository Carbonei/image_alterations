import time
import zmq 
from PIL import Image

#set up communication
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8888")

#loop for communication
while True:
    #get service
    service = socket.recv()
    socket.send_string("ready for file name")
    #time.sleep(0.3)
    
    file = socket.recv()
    time.sleep(0.3)

    image = Image.open(file.decode())
    file = file.decode()

    #remove file extentions
    image_name = file.removesuffix(".png")
    image_name = file.removesuffix(".jpg")
    
    #ensure .png format
    image_name = str(image_name + ".png")
    
    image.save(image_name)
    
    
    

    
    if len(service) > 0 and len(file) > 0:
        #quit on Q
        if service.decode() == 'Q' or file == "Q": 
            break
        

        elif service.decode() == "resize":
            socket.send_string("ready for width")
            width = socket.recv()
            width = int(width.decode())

            time.sleep(0.3)
            socket.send_string("ready for height")
            height = socket.recv()
            height = int(height.decode())

            size = (width, height)
            alt_image = image.resize(size)
            alt_image.save("alt_image.png")
            

        elif service.decode() == "rotate":
            socket.send_string("ready for rotation degrees")
            time.sleep(0.3)
            
            degree = socket.recv()
            degree = degree.decode()
            
            alt_image = image.rotate(int(degree))
            alt_image.save("alt_image.png")

        elif(service.decode() == "recolor"):
            #Reduce to 16 colors to make the image more 'gamey'
            alt_image = image.quantize(4)
            alt_image.save("alt_image.png")
          
            

          
        else:
            socket.send_string("Service not found")
            degree = socket.recv()
            socket.send_string("Services: scale, rotate, ")
            break
        socket.send_string("./alt_image.png")
  

#end communication
context.destroy()
