import socket
import time

# PORT SCANNER Default Version.

class Default_PortSacnner:

    def __init__(self):

        # we are going to make a socket object with default settings which will get two arguments
        # first argument AF_INET refers to the address family of ipv4 and
        # # second argument SOCK_STREAM refers  connection oriented tcp protocoil.
        self.User_Socket = self.Building_Socket()

        # Requesting User to provide TARGET IP for Scanning.
        self.Print_Output(msg = "Please Provide Target IP Address or Domain Name")
        self.Host = self.Obtaining_UserInput(Type = str)

        # Asking for ports range to user.
        self.Print_Output(msg = "Please Provide ports range to scan")
        self.Starting_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Enter StartingPort of Port Range")
        self.Ending_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Enter LastPort of Port Range")

        # Capturing Starting Time.
        self.ObservedTime = self.Observe_Time()

        # Port_Scanning method will scan all the ports of the target and will display the ports which are opened and vulnerable.
        self.Opened_PortsList = self.Port_Scanning(self.User_Socket, self.Host, self.Starting_Port_Range, self.Ending_Port_Range)

        # Actual_TimeTaken_In_Scan variable will store accurate time that have been taken by port scanning process.
        Actual_TimeTaken_In_Scan = self.ObservedTime - time.time()

        # Writing output of Actual_TimeTaken_In_Scan and Opened_PortList on console for user.
        self.Print_Output(msg = Actual_TimeTaken_In_Scan)
        self.Print_Output(messages = self.Opened_PortsList)

    # Building_Socket method build User socket and also return User Socket.
    def Building_Socket(self):
        try:
            self.user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return self.user_socket
        except:
            print("something wrong with the socket library")

    # Getting_UserInput method get information from user according to its Type parameter.
    def Obtaining_UserInput(self, Type = None, msg = ""):
        while True:
            try:
                User_Info = Type(input(msg))
                return User_Info
            except:
                print('INVALID INPUT')

    # Observe_Time method will record the staritng time of PortScanning process.
    def Observe_Time(self):
        try:
            Time = time.time()
            return Time
        except:
            print("error occured in time library")

    # Port_Scanning method will scan Starting_port to Ending_Port range and will return Opened_PortsList.
    def Port_Scanning(self, sock, Host, Starting_Port, Ending_Port):
        self.Opened_PortsList = []
        for port in range(Starting_Port, Ending_Port):
            HostAndPort_Tuple = (Host, port)
            try:
                sock.connect(HostAndPort_Tuple)
                self.Opened_PortsList.append(port)
                print(port,"Port Opened")
            except:
                print(port,"Port Closed")
        return self.Opened_PortsList

    # Print_Output will print msg and mesaages on console and return None.
    def Print_Output(self, msg = "", messages=None):
        if messages:
            for msg in messages:
                print(msg)
        if msg:
            print(msg)

scanner=Default_PortSacnner()