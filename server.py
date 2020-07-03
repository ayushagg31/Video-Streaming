import socket, videosocket
from videofeed import VideoFeed
import random
import cv2
import numpy
import io
from PIL import Image

class Server:
    def __init__(self,port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("", port))
        self.server_socket.listen(5)
        #self.videofeed = VideoFeed(1,"server",1)
        print "TCPServer Waiting for client on port ", port

    def start(self):
        while 1:
        	client_socket, address = self.server_socket.accept()
        	print "I got a connection from ", address
        	vsock = videosocket.videosocket(client_socket)
        	i=0
        	while True:
        		frame_bytes	=vsock.vreceive()
        		#print(frame_bytes)
        		pil_bytes = io.BytesIO(frame_bytes)
        		pil_image = Image.open(pil_bytes)
        		cv_image = cv2.cvtColor(numpy.array(pil_image),cv2.COLOR_RGB2BGR)
       			cv2.imshow('preview',cv_image)
       			if cv2.waitKey(1) & 0xFF == ord('q'): 
       				break 
        		#self.videofeed.set_frame(frame)
                #frame=self.videofeed.get_frame()
                #vsock.vsend(frame)

if __name__=="__main__":
	port = random.randint(1000,9999)
	server = Server(port)
	server.start()
