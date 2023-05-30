# backend/network_check.py

import socket
import speedtest

def perform_network_check():
    try:
        # Attempt to connect to a well-known host (e.g., Google's public DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True  # Network connection is successful
    except socket.error:
        return False  # Network connection failed

def check_network_speed():
    speed_test = speedtest.Speedtest()
    speed_test.get_best_server()
    download_speed = speed_test.download() / 1000000  # Convert to Mbps
    upload_speed = speed_test.upload() / 1000000  # Convert to Mbps
    
    return True, f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f}"