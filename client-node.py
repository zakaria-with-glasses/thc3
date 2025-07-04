import socket
from typing import List, Union

class ClientNode:
    def __init__(self, exposed_port):
        self.port = exposed_port
        self.ip = socket.gethostbyname(socket.gethostname())
        print(f"ip: {self.ip}, port: {self.port}")
        self.recv_req_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.avaliableports = [1049, 1109, 1193]
        self.avaliable_endpoints = self.port_supervisor(action="INIT")


    def port_supervisor(self, action:str=None) -> dict|int|None:
        if action is None:
            return None
        
        if action == "INIT":
            endpoints = {}
            for i in self.avaliableports:
                endpoints[str(i)] = 0

            return endpoints
        
        if action == "PSH":
            for k in self.avaliable_endpoints:
                if self.avaliable_endpoints[k] != 5:
                    self.avaliable_endpoints[k] += 1
                    return int(k, 10)
                
            return None
        


    def continuous_recv(self):
        self.recv_req_socket.bind((self.ip, self.port))
        while True:
            # aftere the message is recieved the
            # message contains the the port to which the TCP connection will be made.
            # msg: "method,ip";  example: "REQ,192.168.111.201"
            # each connection port can hold 5 symultanious requests                
            # to each client we associate a channel number to which he and only him can send request to that specific channel.

            data, binder = self.recv_req_socket.recvfrom(20)
            (method, ip) = data.decode().split(",")[:2]
                
            if method.lower() == "req":
                if ip.strip() == binder[0]:
                    port_to_connect = self.port_supervisor(action="PSH")
                    if self.avaliableports != []:
                        self.recv_req_socket.sendto(f"p:{port_to_connect}".encode(), binder)
                    else:
                        self.recv_req_socket.sendto("FFFF".encode(), binder)
                            
            break
            
        
zakaria = ClientNode(50505)
zakaria.continuous_recv()
