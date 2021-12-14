import fire
import Asyncio_PortScanner
import MultiProcessing_PortScanner
import MultiThreaded_PortScanner
import Port_Scanner

class Network_PortScanner:
    
    def DefaultPortScanner(self, DefaultPortScanner):
        if DefaultPortScanner == "Activate":
            return Port_Scanner.core()
        else:
            return "Run python3 Call.py - -- --help for more information about commands"

    def MultiThreadedPortScanner(self, MultiThreadedPortScanner):
        if MultiThreadedPortScanner == "Activate":
            return MultiThreaded_PortScanner.core()
        else:
            return "Run python3 Call.py - -- --help for more information about commands"

    def MultiProcessingPortScanner(self, MultiProcessingPortScanner):
        if MultiProcessingPortScanner == "Activate":
            return MultiProcessing_PortScanner.core()
        else:
            return "Run python3 Call.py - -- --help for more information about commands"

    def AsyncioPortScanner(self, AsyncioPortScanner):
        if AsyncioPortScanner == "Activate":
            return Asyncio_PortScanner.core()
        else:
            return "Run python3 Call.py - -- --help for more information about commands"

if __name__ == "__main__":
    fire.Fire(Network_PortScanner)

        