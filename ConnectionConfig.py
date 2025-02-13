# This Python file uses the following encoding: utf-8
from bleak import BleakClient
import asyncio
from qasync import asyncSlot
from functools import partial


class ConnectionConfig:

    def __init__(self):

        self.client = None

    @asyncSlot(str)
    async def connectAndDiscoverServices(self, address):
        print(f"Connecting to BLE device at {address}...")

        self.client = BleakClient(address)
        try:

            await self.client.connect()
            print("Connected to", address)
            print("Discovering services...")
            services = self.client.services  # Explicitly call get_services() here if needed
            
            if services:

                for service in services:
                    print(f"Service: {service.uuid}")
                    for char in service.characteristics:
                        print(f"    Characteristic: {char.uuid} | Properties: {char.properties}")
            else: 
                
                print("service not found")
                # # Check if the characteristic supports writin
                #     selected_characteristic = selected_service.characteristics[1]
                #     if "read" in selected_characteristic.properties:
                #         print(f"Reading from characteristic: {selected_characteristic.uuid}")
                 #         value = await client.read_gatt_char(selected_characteristic.uuid)
                #         print(f"Read value: {value.hex()}")
                # else:
                #     print("Selected characteristic does not support writing.")
            return services

        except Exception as e:
            print(f"Error: {e}")
            raise Exception("something went wrong")
    
    @asyncSlot(str)
    async def writeChar(self, char, data):

        if not isinstance(data, bytes):
            data = bytes(data, "utf-8")
        
        print(char)

        if "write" in char.properties:

            print(f"Selected characteristic: {char.uuid}")
            await self.client.write_gatt_char(char.uuid, data)
            print("Data written successfully.")

    
    @asyncSlot(str)
    async def readChar(self, characteristic):
        if "read" in characteristic.properties:
                    print(f"Reading from characteristic: {characteristic.uuid}")
                    value = await self.client.read_gatt_char(characteristic.uuid)
                    print(f"Read value: {value.hex()}")
    
    @asyncSlot(str)
    async def notify(self, label, characteristic_uuid):
        
        if self.client.is_connected:

            await self.client.start_notify(
                characteristic_uuid,
                partial(self.notificationHandler, label=label)
            )
            # await asyncio.sleep(2)

            # await self.client.stop_notify(characteristic_uuid)
            # print("stopped notification")

    def notificationHandler(self, sender, data, label):
        
        data = data.decode('utf-8', errors='ignore')

        print(f"sender : {sender}       data : {data}")
        label.setText(data)

    