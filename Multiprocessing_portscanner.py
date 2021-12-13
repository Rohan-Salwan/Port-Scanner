from multiprocessing import Pool
from portscanner import Default_PortSacnner

# MULTIPROCESSING PORT SCANNER
class MultiProcessing_PortScanner(Default_PortSacnner):

    def __init__(self):

        self.Print_Output(msg = "Please provide target ip address or domain name below")

        # Requesting user to provide TARGET IP for scanning.
        self.host = self.Obtaining_UserInput(Type=str)

        self.Print_Output(msg = 'Type port numbers range down below')

        # Requesting user to provide PortRange for scanning.
        Starting_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Please provide StartingPort of Range")
        Ending_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Please provide LastPort of Range")

        self.Print_Output(msg="User can increase the speed of PortScanner by increasing Process count")

        self.Print_Output(msg="User can create maximum 500 processes")

        # Requesting user to provide process count which will eventually control the speed of portscanner.
        self.Process_Count = self.MultiProcess_Controller(Type=int)

        # Capturing Starting Time.
        self.Recorded_Time = self.Observe_Time()

        # Initializing process of portscanner on selected target.
        self.MultiProcessing_Pool(Starting_Port_Range, Ending_Port_Range, self.Process_Count)

        # Displaying time taken of entire scanning process.
        self.Print_Output(msg = self.Recorded_Time-self.Observe_Time())

    # port_scanner method will create a client socket which will try to connect with server socket.
    def port_scanner(self, port):
        self.User_Socket = self.Building_Socket()
        HostAndPort_Tuple = (self.host,port)
        try:
            Connection =self.User_Socket.connect(HostAndPort_Tuple)
            print(port,"Port is Opened")
            Connection.close()
        except:
            pass

    # Multiprocessing_Pool method will create a pool of several processes and also it will start whole processes parallelly.
    def MultiProcessing_Pool(self, FirstPort_of_Range, LastPort_of_Range, Process_Count):
        with Pool(processes = Process_Count) as pool:
            pool.map(self.port_scanner, range(FirstPort_of_Range, LastPort_of_Range))

    # MultiProcess_Controller method will get process count from user eventually its gonna control speed of PortScanner.
    def MultiProcess_Controller(self, Type =None, msg = ""):
        while True:
            try:
                Number_of_Processes = Type(input(msg))
                if Number_of_Processes > 500 or Number_of_Processes < 1:
                    self.Print_Output(msg = "Invalid Input")
                else:
                    return Number_of_Processes
            except:
                self.Print_Output(msg="Invalid Input")
