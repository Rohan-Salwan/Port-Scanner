import unittest
from unittest.mock import patch

class TestMultiThreadedPortScanner(unittest.TestCase):

    def test_MultiThreadedPortScanner(self):
        with patch("MultiProcessing_PortScanner.MultiProcessing_PortScanner.port_scanner") as port_scanner:
            port_scanner.return_value = None
        self.assertIsNone(port_scanner())

    def test_MultiProcessingPool(self):
        with patch("MultiProcessing_PortScanner.MultiProcessing_PortScanner.MultiProcessing_Pool") as MultiProcessing_Pool:
            MultiProcessing_Pool.return_value = None
        self.assertIsNone(MultiProcessing_Pool())

    def test_MultiProcessController(self):
        with patch("MultiProcessing_PortScanner.MultiProcessing_PortScanner.MultiProcess_Controller") as Multiprocessing_Controller:
            Multiprocessing_Controller.return_value = 500
        self.assertEqual(Multiprocessing_Controller(),500)
