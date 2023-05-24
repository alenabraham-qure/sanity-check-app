# frontend/gui.py

import tkinter as tk
import backend.system_info as system_info
import backend.firewall as firewall

def show_system_info():
    info = system_info.check_system_info()
    info_text = ""
    for key, value in info.items():
        info_text += f"{key}: {value} bytes\n"

    system_info_label.config(text=info_text)

def show_firewall_status():
    firewall_status = "Enabled" if firewall.is_firewall_enabled() else "Disabled"
    firewall_label.config(text=firewall_status)

def create_window():
    # Create the main window
    window = tk.Tk()
    window.title("Sanity Check")
    window.geometry("400x300")

    # Create labels for system information and firewall status
    system_info_label = tk.Label(window, text="System Information:")
    system_info_label.pack(pady=10)

    firewall_label = tk.Label(window, text="Firewall Status:")
    firewall_label.pack(pady=10)

    # Create buttons to trigger the checks
    system_info_button = tk.Button(window, text="Check System Info", command=show_system_info)
    system_info_button.pack(pady=10)

    firewall_button = tk.Button(window, text="Check Firewall Status", command=show_firewall_status)
    firewall_button.pack(pady=10)

    return window
