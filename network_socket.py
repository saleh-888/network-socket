import socket

ser_address = input("ENTER THE SERVER IP ADDRESS: ")
ser_port = int(input("ENTER THE SERVER PORT: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ser_address, ser_port))
s.listen(1)

print("SERVER START!! WATING FOR CONNECTIONS...")
connection, address = s.accept()
print("THE CLINT IS CONNECTIONS WITH ADDRESS: ", address)

while 1:
    data = connection.recv(1024)
    if not data:break
    connection.sendall(b'-- MESSAGE RECEVED --\n')
    print(data.decode('UTF-8'))
connection.close()