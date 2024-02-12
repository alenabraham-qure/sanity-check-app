# backend/system_info.py

import platform
import psutil

def get_total_ram():
    return psutil.virtual_memory().total

def get_total_storage():
    total, _, _ = psutil.disk_usage('/')
    return total

def get_system_bit():
    return platform.architecture()[0]

def check_system_info():
    total_ram = get_total_ram()
    total_storage = get_total_storage()
    system_bit = get_system_bit()

    system_info = {
        'Total RAM': total_ram,
        'Total Storage': total_storage,
        'System Bit': system_bit
    }

    return system_info
