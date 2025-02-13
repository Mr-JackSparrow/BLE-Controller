# BLE Controller

A Bluetooth Low Energy (BLE) Controller built using Python, Bleak, and Qt to scan, connect, and interact with BLE devices.

## Features
- Scan for available BLE devices.
- Connect to a selected device.
- Discover and list services and characteristics.
- Read and write data to characteristics.
- Enable notifications for real-time data updates.
- Asynchronous communication for efficient interaction.

## Technologies Used
- **Python**: Core language for development.
- **Bleak**: Cross-platform BLE library for device communication.
- **Qt (PySide6)**: GUI framework for an interactive interface.
- **QAsync**: Integrates Qt’s event loop with Python’s asyncio for smooth operation.

## Installation

### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-JackSparrow/BLE-Controller.git
   cd BLE-Controller
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Click **SCAN** to discover nearby BLE devices.
3. Select a device and click **CONNECT** to establish a connection.
4. View available services and characteristics.
5. Read or write data to a characteristic.
6. Enable notifications to receive real-time updates.

## Project Structure
```
BLE-Controller/
│-- ui_form.py            # UI generated from Qt Designer
│-- main.py               # Main application logic
│-- ScannerConfig.py      # Handles BLE device scanning
│-- ConnectionConfig.py   # Manages BLE connection & communication
│-- requirements.txt      # Required dependencies
│-- README.md             # Project documentation
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions
Feel free to fork this repository and submit pull requests to improve functionality.

## Contact
For any issues or suggestions, reach out via [yashjadhav.scoe.comp@gmail.com].

