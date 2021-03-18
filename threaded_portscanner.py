try:    
    import threading
    import socket
    from queue import Queue
    import time
except:
    print("Error occured in modules")
# Threaded port scanner 
# with queue data structure and threading library
# using threading.lock to lock the individual data of thread 
print_lock=threading.Lock()
print("enter ip address or domain name below")
host=input()
print("enter port range down below")
while 0<1:
    try:
        starting_port=int(input("Enter firstport of port range"))
        break
    except:
        print("invalid input")
while 0<1:
    try:
        ending_port=int(input("Enter lastport of port range"))
        break
    except:
        print("invalid input")
# Making socket with the help of socket library and trying to connect with server
def ps(port):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con=client.connect((host,port))
        with print_lock:
            print("port",port,"is open")
        con.close()
    except:
        pass
# In threader function thread is getting a work from queue and assigning it to ps(portscanner) function and all threads going to do this process untill the queue's empty. 

def threader():
    while q.empty()!=True:
        work=q.get()
        ps(work)
        q.task_done()

# Making a queue object and using it to store work for workers and threads are playing role of workers and threads are  going to build by threading.thread.
try:
    start=time.time()
except:
    print("Error occured in time library")
try:
    q=Queue()
except:
    print("Error occured in queue library")

for work in range(starting_port,ending_port):
    q.put(work)

print("wanna enhance port scanner speed so type no of threads below")
while 0<1:
    try:
        print("Maximum threads limit 1000")
        print("Enter thread count below")
        threads=int(input())
        if threads >1000:
            pass
        else:
            break
    except:
        print("invalid input")
for thread in range(threads):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()

q.join()
print(start-time.time())
