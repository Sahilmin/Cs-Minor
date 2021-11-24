import socket

# creating a socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5575))

message1 = s.recv(1024).decode()
message2 = s.recv(1024).decode()
message3 = s.recv(1024).decode()

print('Message from Server: ', message1)
print(': ',message2)
print(': ',message3)

s.close()
