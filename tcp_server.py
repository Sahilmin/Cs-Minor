import socket

# creating a socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the address specified as parameter (host,portno) so that server binds to the client
s.bind((socket.gethostname(), 5575))
s.listen(5)
# while connection is true

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!!")
    messageforclient1 = 'An old silent pond.'
    messageforclient2 = 'A frog jumps into the pond-Splash!'
    messageforclient3 = 'Silence again.'
    clientsocket.send(messageforclient1.encode())
    clientsocket.send(messageforclient2.encode())
    clientsocket.send(messageforclient3.encode())
