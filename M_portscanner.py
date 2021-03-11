import socket
import multiprocessing
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

processes=[]
# Main function will create several processes and also it will start whole processes parallel.
def main():
    for port in range(1,range_port): 
        process = multiprocessing.Process(target=ps, args=[port])
        process.daemon=True
        process.start()
        processes.append(process)
    for processe in processes:
        processe.join()
main()
print(start-time.time())
