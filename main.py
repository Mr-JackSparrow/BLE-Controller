# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtBluetooth import QBluetoothDeviceInfo
from bleak.backends.service import BleakGATTService, BleakGATTCharacteristic

import asyncio
from qasync import QEventLoop

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main
from ScannerConfig import Scanner
from ConnectionConfig import ConnectionConfig

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.btnOnOff = self.ui.btnOnOffBluetooth
        self.listDevices = self.ui.listAvailableDevices
        self.listServices = self.ui.listAvailableServices
        self.listChar = self.ui.listAvailableChar
        self.btnConnect = self.ui.btnConnect
        self.txtWrite = self.ui.textWriteData
        self.labelReadData = self.ui.labelReadData
        self.btnInput = self.ui.btnInput

        self.btnOnOff.clicked.connect(self.onOff)
        self.btnConnect.clicked.connect(self.scanConDiscon)
        self.btnInput.clicked.connect(self.writeData)
        self.listDevices.itemClicked.connect(self.onItemClicked)
        self.listServices.itemClicked.connect(self.onItemClicked)
        self.listChar.itemClicked.connect(self.onItemClicked)
        # self.btnUpload.clicked.connect()

        self.scanner = Scanner()
        self.scanner.agent.finished.connect(self.onScanningFinished)
        self.devicesList = []
        self.selectedDevice = None

        self.connector = ConnectionConfig()
        self.serviceList = []
        self.charList = []
        self.selectedService = None
        self.selectedChar = None

    
    def onOff(self, checked):

        if checked:

            self.btnOnOff.setText("ON")
        else:

            self.btnOnOff.setText("OFF")

    def scanConDiscon(self):

        name = self.btnConnect.text()

        if "SCAN" == name:

            self.scanner.start_scan()
            self.btnConnect.setText("CONNECT")
            self.btnConnect.setDisabled(True)
        elif "CONNECT" == name and None != self.selectedDevice:

            if self.selectedDevice.address():

                try:

                    self.serviceList = asyncio.ensure_future(self.fetchAndSetServiceList())

                except Exception as e: 
                    print(f"error : {e}")

        elif "DISCONNECT" == name:

            self.btnConnect.setText("SCAN")
    
    def onScanningFinished(self):

        self.btnConnect.setDisabled(False)
        self.devicesList = self.scanner.devices

        if self.devicesList:
            
            for device in self.devicesList:

                item = QListWidgetItem(device.name() or "Unknown Device")
                item.setData(Qt.ItemDataRole.UserRole, device)
                self.listDevices.addItem(item)


    def onItemClicked(self, item):

        if item:

            data = item.data(Qt.ItemDataRole.UserRole)

            print(f"line 107 {data}")

            
            if isinstance(data, QBluetoothDeviceInfo):
        
                self.selectedDevice = item.data(Qt.ItemDataRole.UserRole)
            elif isinstance(data, BleakGATTService):
            
                self.selectedService = item.data(Qt.ItemDataRole.UserRole)
                print(f"line 118 {self.selectedService}")
                if None != self.selectedService:
                    self.charList = self.selectedService.characteristics
            
                    if self.charList:
                        
                        for chars in self.charList:
                            print(f"line 126 {type(chars)}")
                            
                            name = ", ".join(chars.properties)
                            item = QListWidgetItem(name)
                            item.setData(Qt.ItemDataRole.UserRole, chars)
                            self.listChar.addItem(item)
                            print(f"line 133 {item.data(Qt.ItemDataRole.UserRole)}")
            elif isinstance(data, BleakGATTCharacteristic):
                print("hello")
                self.selectedChar = item.data(Qt.ItemDataRole.UserRole)
                print(self.selectedChar)

    async def fetchAndSetServiceList(self):

        self.serviceList = await self.connector.connectAndDiscoverServices(self.selectedDevice.address().toString())

        self.btnConnect.setText("DISCONNECT")

        if self.serviceList:

                    for service in self.serviceList:
                        
                        item = QListWidgetItem(service.uuid)
                        item.setData(Qt.ItemDataRole.UserRole, service)
                        self.listServices.addItem(item)
    
    def writeData(self):

        data = self.txtWrite.toPlainText()

        if data:
            print(self.selectedChar)
            asyncio.ensure_future(self.connector.writeChar(self.selectedChar, data))
            asyncio.ensure_future(self.connector.notify(self.labelReadData, "6e400003-b5a3-f393-e0a9-e50e24dcca9e"))
        else:

            self.txtWrite.setPlainText("No data to write")

    




if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    widget = Main()
    widget.show()
    
    with loop:
        loop.run_forever()

    sys.exit(app.exec())
