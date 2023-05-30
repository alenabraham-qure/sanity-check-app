# backend/system_info.py

import platform
import psutil

def get_total_ram():
    return psutil.virtual_memory().total / (1024**3)  # Convert bytes to GB

def get_total_storage():
    total = psutil.disk_usage('/').total / (1024**3)  # Convert bytes to GB
    return total

def get_system_bit():
    return platform.architecture()[0]

def check_system_info():
    total_ram = get_total_ram()
    total_storage = get_total_storage()
    system_bit = get_system_bit()

    system_info = {
        'Total RAM': f'{total_ram:.2f} GB',
        'Total Storage': f'{total_storage:.2f} GB',
        'System Bit': system_bit
    }

    return system_info
