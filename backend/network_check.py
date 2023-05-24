# backend/network_check.py

import socket

def perform_network_check():
    try:
        # Attempt to connect to a well-known host (e.g., Google's public DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True  # Network connection is successful
    except socket.error:
        return False  # Network connection failed
