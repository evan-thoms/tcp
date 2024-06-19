#Basic TCP Client, but makes assumptions that the connection will always succeed 
## and that the server expects us to send data first

import socket

targetHost = "www.google.com"
targetPort = 80
#creates socket object, specifying that we are using IPV4 and that it will be TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect client
client.connect((targetHost,targetPort))
#send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#receive data
response = client.recv(4096)

print(response.decode())
client.close()