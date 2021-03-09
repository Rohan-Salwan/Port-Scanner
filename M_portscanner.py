import socket
import multiprocessing
import time
from queue import Queue

target = input()
while 0<1:
    try:
        range_port=int(input())
        break
    except:
        print("invalid input")

def ps(port):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr=(target,port)
    try:
        con=client.connect(addr)
        print(port,"port is opened")
        con.close()
    except:
        pass

start=time.time()
processes=[]
def main():
    for work in range(1,range_port):
        process = multiprocessing.Process(target=ps,args=[work])
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
main()
print(start-time.time())
