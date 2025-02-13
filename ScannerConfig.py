# This Python file uses the following encoding: utf-8
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo
from PySide6.QtCore import QObject, Signal

class Scanner(QObject): 

    def __init__(self):
        super().__init__()
        self.agent = QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.device_discovered)
        self.agent.finished.connect(self.scan_completed)
        self.devices = []

    def start_scan(self):
        print("Starting Bluetooth scan...")
        self.devices = []
        self.agent.start()

    def device_discovered(self, device: QBluetoothDeviceInfo):
        self.devices.append(device)

    def scan_completed(self):
        print("Scan completed!")
