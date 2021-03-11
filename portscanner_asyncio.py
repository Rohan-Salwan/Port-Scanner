import socket
import asyncio
import time
# PORT SCANNER ASYNCIO VERSION
# getting target address and ports information from user.
print("Enter ip address or domain name down below")
target=input()
print("Enter ports range below")
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
# firstly socket.socket class will create a client object with some arguments.
# In ps function, client will try to connect with target port services.
# async is just defining ps function as coroutine function.
async def ps(port):
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr=(target,port)
        try:
            client.connect(addr)
            print(port,"port opened")
        except:
            print(port,"port closed")

# In main function event loop object will create some tasks and these tasks are going to store in event loop.
async def psmain(starting_port,ending_port):
    while starting_port< ending_port:
        if starting_port+1==ending_port:
            break
        task1=loop.create_task(ps(starting_port))
        task2=loop.create_task(ps(starting_port+1))
        await asyncio.wait([task1,task2])
        starting_port+=1

# using time library to calculate the time of port scanning process.
start = time.time()
# Event loop is going to create with the help of asyncio library method (get_event_loop().)
# run_untill_complete method will run the event loop untill its completion.
loop=asyncio.get_event_loop()
loop.run_until_complete(psmain(starting_port,ending_port))
loop.close()
print(start-time.time())
