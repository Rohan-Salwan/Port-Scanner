import socket

# PORT SCANNER
# importing socket library with that we are going to make a socket object with default settings# which will get two arguments first argument AF_INET refers to the address family of ipv4 and # second argument SOCK_STREAM refers  connection oriented tcp protocol. 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HOST IS OUR TARGET
# Port scanner will scan all of the ports of the target and tell us about those ports which are opened 
host="192.168.1.2"
ports = 65535
# l is a list of opening ports 
l=[]
for e in range(ports):
    dd=(host,e)
    try:
        client.connect(dd)
        l.append(e)
        print("port opennnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    except:
        print("port closed")
print(l)
print("opened ports")


