import socket
s = socket.socket()
s.bind(("localhost", 8000))
s.listen(5)
c, addr = s.accept()
size=int(input("Enter the number of frames to send:"))
l=list(range(size))
s=int(input("Enter windows size:"))
st=0
i=0
while True:
  while (i<len(l)):
    st+=s
    c.send(str(l[i:st]).encode())
    ack = c.recv(1024).decode()
    if ack:
        print(ack)
        i+=s

