import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    try:
        
        msg = input("message> ")
        s.sendto(msg.encode(), ("192.168.1.13",50505))
        data, server = s.recvfrom(1024)
        print(data, server)
    except KeyboardInterrupt:
        exit()

