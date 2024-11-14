import serial.tools.list_ports


def list_all_com_ports():
    """
    This file only lists COM ports with the device and COM port for known VID/PID pairs. (i.e., OpenBCI Cyton Board Dongle)
    """

    # Known VID/PID pairs (example includes OpenBCI devices)
    known_vid_pid_pairs = [
        (0x0403, 0x6015),  # Cyton with FTDI chip
    ]

    ports = list(serial.tools.list_ports.comports())
    compatible_ports = []

    if not ports:
        print("No COM ports found.")
    else:
        for port in ports:
            # Check if the port's VID and PID match any known VID/PID pairs
            if (port.vid, port.pid) in known_vid_pid_pairs:
                print(f"Device: {port.device}")
                print(f" - Serial Number: {getattr(port, 'serial_number', 'N/A')}")
                print(f" - Description: {port.description}")
                print("")
                
                # Collect compatible port details if needed
                compatible_ports.append({
                    'port': port.device,
                    'serial_number': getattr(port, 'serial_number', 'N/A'),
                    'description': port.description
                })

    if not compatible_ports:
        print("No compatible devices found.")

    return compatible_ports

# Run this function to get a detailed list of matching COM port information
list_all_com_ports()



# --------------------------
# Original COM Finder:
# --------------------------

# def list_all_com_ports():
#     """
#     This function scans all USB ports and lists detailed information for each port.
#     """
    
#     ports = list(serial.tools.list_ports.comports())
#     if not ports:
#         print("No COM ports found.")
#     else:
#         for port in ports:
#             print(f"Device: {port.device}")
#             print(f" - Serial Number: {getattr(port, 'serial_number', 'N/A')}")
#             print(f" - Description: {port.description}")
#             print(f" - Manufacturer: {getattr(port, 'manufacturer', 'N/A')}")
#             print(f" - VID:PID: {getattr(port, 'vid', 'N/A')}:{getattr(port, 'pid', 'N/A')}")
#             print(f" - HWID: {port.hwid}")
#             print("")

# # Run this function to get a detailed list of COM port information
# list_all_com_ports()
