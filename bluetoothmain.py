from PySide6.QtCore import QCoreApplication, QTimer, Signal, QObject
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo
from bleak import BleakClient
import asyncio
from qasync import QEventLoop, asyncSlot

class BluetoothScanner(QObject):
    scan_finished = Signal()
    device_chosen = Signal(str)

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
        address = device.address().toString()
        name = device.name() or "Unknown Device"
        print(f"Discovered: {name} - {address}")
        self.devices.append((name, address))

    def scan_completed(self):
        print("Scan completed!")
        if self.devices:
            for i, (name, address) in enumerate(self.devices):
                print(f"Device {i}: {name} - {address}")
            print("Enter the device number to connect:")
        else:
            print("No devices found.")
        self.scan_finished.emit()

@asyncSlot(str)
async def connect_and_write_to_device(address):
    print(f"Connecting to BLE device at {address}...")
    try:
        async with BleakClient(address) as client:
            print("Connected to", address)

            # Discover services
            print("Discovering services...")
            services = client.services  # Explicitly call get_services() here
            
            if services:
                print("Services:")
            else: print("service is null")
            
            for service in services:
                print(service)
                print(f"Service: {service.uuid}")
                for char_idx, char in enumerate(service.characteristics):
                    print(f"  [{char_idx}] Characteristic: {char.uuid} | Properties: {char.properties}")

            # # Get user input for service and characteristic selection
            # service_index = int(input("Enter the service index to write to: "))
            # selected_service = list(services)[service_index]  # Convert to list for indexing
            
            # characteristic_index = int(input("Enter the characteristic index to write to: "))
            # selected_characteristic = selected_service.characteristics[characteristic_index]
            
            # # Check if the characteristic supports writing
            # if "write" in selected_characteristic.properties:
            #     # Write data to the characteristic
            #     print(f"Selected characteristic: {selected_characteristic.uuid}")
            #     data = bytes(input("Enter the data to send: "), "utf-8")
            #     await client.write_gatt_char(selected_characteristic.uuid, data)
            #     print("Data written successfully.")

            #     selected_characteristic = selected_service.characteristics[1]

            # else:
            #     print("Selected characteristic does not support writing.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Operation completed. Exiting application...")
        asyncio.get_event_loop().stop()

async def notification_handler(sender, data):
    print(f"Notification from {sender}: {data.decode('utf-8')}")


def main():
    app = QCoreApplication([])

    # Use QEventLoop to integrate asyncio and PySide6 event loops
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    scanner = BluetoothScanner()

    async def on_scan_finished():
        device_index = int(input())
        name, address = scanner.devices[device_index]
        print(f"Selected: {name} - {address}")
        await connect_and_write_to_device(address)

    scanner.scan_finished.connect(lambda: loop.create_task(on_scan_finished()))

    QTimer.singleShot(0, scanner.start_scan)

    with loop:
        loop.run_forever()

if __name__ == "__main__":
    main()
    QCoreApplication.quit()
