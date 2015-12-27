# client
from socket import *
import os
import sys

C_ser = sys.argv[1]
C_ser_port = 1234
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind((C_ser, C_ser_port))
clientSocket.connect((serverName, serverPort))
msg = 'open'
while 1:

	print('Socket', clientSocket.fileno(), 'opened to server', serverName, ':', serverPort)
	msg = raw_input('What is your message? ')

	clientSocket.send(msg)
	if msg == 'exit':
		clientSocket.close()
		break
	response = clientSocket.recv(1024)

	print('Server says:', response)



