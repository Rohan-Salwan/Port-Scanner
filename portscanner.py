import socket
import time

# PORT SCANNER
# importing socket library with that we are going to make a socket object with default settings# which will get two arguments first argument AF_INET refers to the address family of ipv4 and # second argument SOCK_STREAM refers  connection oriented tcp protocoil. 
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("something wrong with the socket library")
# HOST IS OUR TARGET
# Port scanner will scan all of the ports of the target and tell us about those ports which are opened. 
print("Enter target IP address or domain name down below")
host=input()
print("Enter ports range down below which you want to scan")
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
opened_ports_list=[]
try:
    start=time.time()
except:
    print("error occured in time library")
for port in range(starting_port,ending_port):
    dd=(host,port)    
    try:
        client.connect(dd)
        opened_ports_list.append(port)
        print("port opened")
    except:
        print("port closed")
print(start-time.time())
print(opened_ports_list)
print("opened ports")


