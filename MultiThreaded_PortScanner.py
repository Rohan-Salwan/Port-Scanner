import threading
from queue import Queue
from Port_Scanner import Default_PortScanner
import socket

# Threaded Port Scanner
class MultiThreaded_PortScanner(Default_PortScanner):

    def __init__(self):

        # Preparing threading.Lock to lock data of individual thread.
        self.print_lock = self.Thread_Lock()

        self.Print_Output(msg = "Please provide target ip address or domain name below")

        # Requesting user to provide TARGET IP for scanning.
        Host = self.Obtaining_UserInput(Type=str)

        self.Opened_PortsList = []

        self.Print_Output(msg = 'Type port numbers range down below')

        # Requesting user to provide PortRange for scanning.
        Starting_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Please provide StartingPort of Range")
        Ending_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Please provide LastPort of Range")

        self.Queue = self.Building_Queue()

        # Filling Queue with ports one by one serialwise.
        self.PushingPorts_Into_Queue(Starting_Port_Range, Ending_Port_Range, self.Queue)

        # Capturing Starting Time.
        self.RecordedTime = self.Observe_Time()

        self.Print_Output(msg="User can increase the speed of PortScanner by increasing Threads count")

        self.Print_Output(msg="User can create maximum 1000 Threads")

        # Requesting user to provide thread count which will eventually control the speed of portscanner.
        self.Thread_Count = self.MultiThread_Controller(Type=int)

        # Initializing process of portscanner on selected target.
        self.BuildingAndExecution_OF_Threads(self.Thread_Count, Host, self.Queue, self.print_lock)

        # Displaying Opened ports of selected Target.
        self.Print_Output(msg = ("Vulnerable_Ports", self.Opened_PortsList))

        # Displaying time taken of entire scanning process.
        self.Print_Output(msg = self.RecordedTime-self.Observe_Time())

    # port_scanner method will create a client socket which will try to connect with server socket.
    def port_scanner(self, host, port, Lock):
        self.User_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HostAndPort_Tuple = (host,port)
        try:
            connection = self.User_Socket.connect(HostAndPort_Tuple)
            with Lock:
                print("port",port,"is open")
                self.Opened_PortsList.append(port)
            connection.close()
        except:
            pass

    # PoppingPortFromQueue_And_InitilizingPortScanner method will pop port from queue and initialize the port scannner with that port.
    def PoppingPortFromQueue_And_InitilizingPortScanner(self, Host, Queue, Lock):
        while Queue.empty() is not True:
            Port = Queue.get()
            self.port_scanner(Host, Port, Lock)
            Queue.task_done()

    # Building_Queue method will Build Queue to store ports which is requested by user to scan.
    def Building_Queue(self):
        try:
            Queuee = Queue()
            return Queuee
        except:
            print("Error occured in queue library")

    # PushingPorts_Into_Queue method will push every single port into queue which is requested by user to scan.
    def PushingPorts_Into_Queue(self, FirstPort_of_Range, LastPort_of_Range, Queue):
        for port in range(FirstPort_of_Range, LastPort_of_Range):
            Queue.put(port)

    # BuildingAndExecution_OF_Threads method will execute core execution of module.
    def BuildingAndExecution_OF_Threads(self, Threads_Count, Host, queue, Lock):
        for _ in range(Threads_Count):
            Thread = threading.Thread(target=self.PoppingPortFromQueue_And_InitilizingPortScanner, args=(Host, queue, Lock))
            Thread.daemon=True
            Thread.start()
        self.Queue.join()

    # MultiThread_Controller method will get thread count from user eventually its gonna control speed of PortScanner.
    def MultiThread_Controller(self, Type = None, msg = ""):
        while True:
            try:
                Number_of_Threads = Type(input(msg))
                if Number_of_Threads > 1000 or Number_of_Threads < 1:
                    self.Print_Output(msg = "Invalid Input")
                else:
                    return Number_of_Threads
            except:
                self.Print_Output(msg = "Invalid Input")

    # Thread_Lock method build lock for threds.
    def Thread_Lock(self):
        try:
            Lock = threading.Lock()
            return Lock
        except:
            self.Print_Output(msg = "Error in threading lock module")