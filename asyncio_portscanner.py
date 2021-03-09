import socket
import asyncio
import time

target=input()
print("enter ports range below")
while 0<1:
    try:
        port_range=int(input())
        break
    except:
        print("invalid input")

async def ps(port):
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr=(target,port)
        if port==5:
            await asyncio.sleep(10)
        try:
            client.connect(addr)
            print(port,"port opened")
        except:
            print(port,"port closed")
async def main(port_range):
    port=1
    while port < port_range:
        if port+1==port_range:
            break
        task1=loop.create_task(ps(port))
        task2=loop.create_task(ps(port+1))
        await asyncio.wait([task1,task2])
        port+=1
start=time.time()
loop=asyncio.get_event_loop()
loop.run_until_complete(main(port_range))
loop.close()

print(start-time.time())
