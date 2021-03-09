import threading
import socket
from queue import Queue
import time
# Threaded port scanner 
# with queue data structure and threading library
# using threading.lock to lock the individual data of thread 
print_lock=threading.Lock()
print("enter ip address or domain name below")
host=input()
print("enter port range down below")
while 0<1:
    try:
        ports=int(input())
        break
    except:
        print("invalid input")
# making socket with the help of socket library and trying to connect with server
def ps(port):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con=client.connect((host,port))
        with print_lock:
            print("port",port,"is open")
        con.close()
    except:
        print(port,"port is closed")
        pass
# In threader function thread is getting a work from queue and assigning it to ps(portscanner) function and all threads going to do this process untill the queue's empty. 

def threader():
    while q.empty()!=True:
        work=q.get()
        ps(work)
        q.task_done()

# making a queue object and using it to store work for workers and threads are playing role of workers and threads are  going to build by threading.thread
start=time.time()
q=Queue()
for work in range(1,ports):
    q.put(work)

for i in range(50):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()

q.join()
print(start-time.time())
