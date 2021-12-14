from queue import Queue
import unittest
from unittest.mock import patch
import threading
from MultiThreaded_PortScanner import MultiThreaded_PortScanner

class TestMultiThreadedPortScanner(unittest.TestCase):

    def test_ThreadingLock(self):
        self.assertEqual(type(MultiThreaded_PortScanner.Thread_Lock(MultiThreaded_PortScanner)), type(threading.Lock()))

    def test_BuildingQueue(self):
        Queue_Instance = MultiThreaded_PortScanner.Building_Queue(MultiThreaded_PortScanner)
        assert isinstance(Queue_Instance, Queue)
    
    def test_PortScanner(self):
        lock=threading.Lock()
        Return_Value = MultiThreaded_PortScanner.port_scanner(MultiThreaded_PortScanner, "192.168.1.1", 1, lock)
        self.assertEqual(Return_Value, None)
    
    def test_PushingPortsIntoQueue(self):
        queue = Queue()
        Return_value = MultiThreaded_PortScanner.PushingPorts_Into_Queue(MultiThreaded_PortScanner, 1, 2, queue)
        self.assertEqual(Return_value, None)

    def test_MultiThreadedController(self):
        with patch("MultiThreaded_PortScanner.MultiThreaded_PortScanner.MultiThread_Controller") as Thread_Controller:
            Thread_Controller.return_value = 1000
        self.assertEqual(Thread_Controller(), 1000)

    def test_PoppingPortFromQueueAndInitilizingPortScanner(self):
        with patch("MultiThreaded_PortScanner.MultiThreaded_PortScanner.PoppingPortFromQueue_And_InitilizingPortScanner") as PopfromQueue:
            PopfromQueue.return_value=None
        self.assertEqual(PopfromQueue(), None)