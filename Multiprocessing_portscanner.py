import socket
from multiprocessing import Pool
import time
# MULTIPROCESSING PORT SCANNER
# getting information of target ip address and port number
print("Enter target ip address or domain name below")
target = input()
print('Type port numbers range down below')
while 0<1:
    try:
        starting_port=int(input("enter starting port"))
        break
    except:
        print('invalid input')
while 0<1:
    try:
        ending_port=int(input("enter ending port"))
        break
    except:
        print("invalid input")
# ps function will create a client socket which will try to connect with server socket.
def ps(port):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr=(target,port)
    try:
        con=client.connect(addr)
        print(port,"port is opened")
        con.close()
    except:
        pass
# Using time library for capturing the whole time of port scanning process.
try:
    start=time.time()
except:
    print("time.time module error")

# Main function will create a pool of several processes and also it will start whole processes parallelly.
def main(starting,ending):
    with Pool(processes=500) as pool:
        pool.map(ps,range(starting,ending))

main(starting_port,ending_port)
print(start-time.time())
