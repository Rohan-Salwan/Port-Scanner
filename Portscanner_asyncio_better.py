try:
    import asyncio
    import time
except:
    print("Eroor occured in modules")
# PORT SCANNER ASYNCIO VERSION
# getting target address and ports information from user.
print("Enter ip address or domain name down below")
target=input()
print("Enter ports range below")
while True:
    try:
        starting_port=int(input("Enter firstport of port range"))
        break
    except:
        print("invalid input")
while True:
    try:
        ending_port=int(input("Enter lastport of port range"))
        break
    except:
        print("invalid input")

async def lob(ip,port):
    try:
        await asyncio.wait_for(asyncio.open_connection(ip,port),timeout=0.01)
        print("port opened",port)
    except:
        print("port closed",port)
async def job(a,b,target):
    while a < b:
        await lob(target,a)
        a+=1

start=time.time()
jo=asyncio.get_event_loop()
jo.run_until_complete(asyncio.wait_for(job(starting_port,ending_port,target),timeout=None))
print(start-time.time())
