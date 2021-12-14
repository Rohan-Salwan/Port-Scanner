import unittest
from unittest.mock import patch
from Asyncio_PortScanner import Asynchronous_PortScanner


class TestAsyncioPortScanner(unittest.TestCase):

    def test_PortScanner(self):
        Return_Value = Asynchronous_PortScanner.Port_Scanner(Asynchronous_PortScanner, "192.168.1.1", 1)
        self.assertIsNotNone(Return_Value)

    def test_RunningSelectedPortsWithAsyncioPortScanner(self):
        Return_Value = Asynchronous_PortScanner.RunningSelectedPorts_With_AsyncioPortScanner(Asynchronous_PortScanner, 1, 2, "192.168.1.1")
        self.assertIsNotNone(Return_Value)

    def test_GettingEventLoop(self):
        with patch("Asyncio_PortScanner.Asynchronous_PortScanner.Getting_EventLoop") as Getting_EventLoop:    
            Getting_EventLoop.return_value = None
        self.assertIsNone(Getting_EventLoop())
    