# import serial.tools.list_ports

# def list_all_com_ports():
#     """
#     Lists all available COM ports with detailed information.
#     """
#     ports = list(serial.tools.list_ports.comports())
#     if not ports:
#         print("No COM ports found.")
#     else:
#         for port in ports:
#             print(f"Device: {port.device}")
#             print(f" - Serial Number: {port.serial_number}")
#             print(f" - Description: {port.description}")
#             print(f" - Manufacturer: {port.manufacturer}")
#             print(f" - VID:PID: {port.vid}:{port.pid}")
#             print("")

# # Run this function to get a detailed list of COM port information
# list_all_com_ports()

import serial.tools.list_ports

def list_all_com_ports():
    """
    Lists all available COM ports with detailed information.
    """
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No COM ports found.")
    else:
        for port in ports:
            print(f"Device: {port.device}")
            print(f" - Serial Number: {getattr(port, 'serial_number', 'N/A')}")
            print(f" - Description: {port.description}")
            print(f" - Manufacturer: {getattr(port, 'manufacturer', 'N/A')}")
            print(f" - VID:PID: {getattr(port, 'vid', 'N/A')}:{getattr(port, 'pid', 'N/A')}")
            print(f" - HWID: {port.hwid}")
            print("")

# Run this function to get a detailed list of COM port information
list_all_com_ports()
