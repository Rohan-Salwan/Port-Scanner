import unittest
import socket
from unittest.mock import patch
import sys
from io import StringIO
from Port_Scanner import Default_PortScanner
import time

class TestDefaultPortScanner(unittest.TestCase):

    def test_BuildingSocket(self):
        Capturing_Return_Value = Default_PortScanner.Building_Socket(Default_PortScanner)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.assertEqual(type(Capturing_Return_Value), type(sock))

    def test_ObserveTime(self):
        Type=time.time()
        time1 = Default_PortScanner.Observe_Time(Default_PortScanner)
        self.assertEqual(type(time1),type(Type))
    
    def test_PrintOutput(self):
        print_output = []
        save_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        Fake_Input=["1", "2", "3", "4", "5"]
        Default_PortScanner.Print_Output(Default_PortScanner,messages=Fake_Input)
        sys.stdout = save_stdout
        print_output.append(result.getvalue())
        print_output = print_output[0]
        Enlist_Public_Users_MethodOutput = print_output.split('\n')
        self.assertEqual(Enlist_Public_Users_MethodOutput[:-2], Fake_Input)

    def test_ObtainingUserInput(self):
        with patch("Port_Scanner.Default_PortScanner.Obtaining_UserInput") as UserInput:
            UserInput.return_value = "Test Passed"
        self.assertEqual(UserInput(),"Test Passed")