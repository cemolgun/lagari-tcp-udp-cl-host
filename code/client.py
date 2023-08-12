import socket

local_ip        = socket.gethostbyname("localhost")
connect_port    = 4578

print("Leave empty if local")
connect_ip = input("Server IP: ")

if connect_ip == "":
    connect_ip = local_ip

connect_adress  = (connect_ip,connect_port)

socket_cl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Send message: 'Exit' to exit.")
while True:
    message = input("Send message: ")

    if message in ["exit", "EXIT", "Exit"]:
        exit()

    message = message.encode("utf-8")
    socket_cl.sendto(message,connect_adress)