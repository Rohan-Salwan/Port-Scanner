import asyncio
from Port_Scanner import Default_PortScanner

# PORT SCANNER ASYNCHRONOUS VERSION
class Asynchronous_PortScanner(Default_PortScanner):
    def __init__(self):
        self.Print_Output(msg = "Please provide target ip address or domain name below")

        # Requesting user to provide TARGET IP for scanning.
        self.host = self.Obtaining_UserInput(Type=str)

        self.Opened_PortsList = []

        self.Print_Output(msg = 'Type port numbers range down below')

        # Requesting user to provide PortRange for scanning.
        Starting_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Please provide StartingPort of Range")
        Ending_Port_Range = self.Obtaining_UserInput(Type = int, msg = "Please provide LastPort of Range")

        # Capturing Starting Time.
        self.Recorded_Time = self.Observe_Time()

        # Initializing asyncio process of portscanner on selected target.
        self.Getting_EventLoop(Starting_Port_Range, Ending_Port_Range, self.host)

        self.Print_Output(msg = ("Vulnerable_Ports -:",self.Opened_PortsList))

        # Displaying time taken of entire scanning process.
        self.Print_Output(msg = self.Recorded_Time-self.Observe_Time())

    # Port_Scanner method will open connection socket which will try to connect with target.
    async def Port_Scanner(self, Host, Port):
        try:
            await asyncio.wait_for(asyncio.open_connection(Host,Port), timeout = 0.01)
            print(Port, "is Opened")
            self.Opened_PortsList.append(Port)
        except:
            pass

    # RunningSelectedPorts_With_AsyncioPortScanner method will iterate through selected ports
    # which is provided by user and also initialized port scanner method with that.
    async def RunningSelectedPorts_With_AsyncioPortScanner(self, FirstPort, LastPort, Target):
        while FirstPort <= LastPort:
            await self.Port_Scanner(Target,FirstPort)
            FirstPort+=1

    # Getting_EventLoop method will bring eventloop to process RunningSelectedPorts_With_AsyncioPortScanner method Asynchronously.
    def Getting_EventLoop(self, FirstPort, LastPort, Target):
        Event_Loop = asyncio.get_event_loop()
        Event_Loop.run_until_complete(asyncio.wait_for(self.RunningSelectedPorts_With_AsyncioPortScanner(FirstPort, LastPort, Target),timeout=None))

def core():
    try:
        Port_Scanner = Asynchronous_PortScanner()
    except:
        print("Error in Asyncio_PortScanner module")