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
        range_port=int(input())
        break
    except:
        print("invalid input")
# ps function will create a client socket which will try to connect with server socket.
def ps(port):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr=(target,port)
    if port ==23:
        pass
    else:
        try:
            con=client.connect(addr)
            print(port,"port is opened")
            con.close()
        except:
            print(port,"port is closed")
            pass
# Using time library for capturing the whole time of port scanning process.
try:
    start=time.time()
except:
    print("time.time module error")

# Main function will create a pool of several processes and also it will start whole processes parallel.
def main(ports_range):
    with Pool(processes=500) as pool:
        pool.map(ps,range(1,ports_range))

main(range_port)
print(start-time.time())
