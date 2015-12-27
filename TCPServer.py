# simple (non-concurrent) TCP server example
from socket import *
serverPort = 12000
listeningSocket = socket(AF_INET, SOCK_STREAM)
listeningSocket.bind(('localhost', serverPort))
listeningSocket.listen(1)
msg = 'open'
print('Server ready, socket', listeningSocket.fileno(), 'listening on localhost :', serverPort)
connectionSocket, addr = listeningSocket.accept()
while 1: 
	msg = connectionSocket.recv(1024)
	if msg == 'exit':
		print('Closing socket', connectionSocket.fileno())
		connectionSocket.close()
		listeningSocket.listen(1)
		print('Server ready, socket', listeningSocket.fileno(), 'listening on localhost :', serverPort)
		connectionSocket, addr = listeningSocket.accept()
	else:
		print('Got connection on socket', connectionSocket.fileno(), 'from', addr[0], ':', addr[1])
		connectionSocket.send(str.encode('Your message is "' + msg + '" '))


