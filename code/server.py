import socket

local_ip = socket.gethostbyname("localhost")
port = 4578

# creating a socket
# family ->  AF_INET : IPv4 adress, AF_INET6 : IPv6.
# type   ->  SOCK_DGRAM : UDP, SOCK_STREAM : TCP
socket_sv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

adress = ("0.0.0.0", port)
socket_sv.bind(adress)

print(f"Server Bind\nAdress:\t{adress}")

while True:
    
    # Waiting for message
    received_bytes, received_adress = socket_sv.recvfrom(1024) # 1 Kb buffer.
    received_msg = received_bytes.decode("utf-8")

    log = open("log.txt","a")
    print(f"Message: {received_msg}\nAdress: {received_adress}")
    print(f"Message: {received_msg}\nAdress: {received_adress}\n", file=log)
    log.close()
