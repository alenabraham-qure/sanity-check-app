# frontend/gui.py

import tkinter as tk
import backend.system_info as system_info
import backend.firewall as firewall
import backend.network_check as network_check

def show_system_info():
    info = system_info.check_system_info()
    info_text = ""
    for key, value in info.items():
        if key == 'Total RAM' or key == 'Total Storage':
            value = value.replace(" bytes", " GB")
        info_text += f"{key}: {value}\n"

    system_info_label.config(text=info_text)


def show_firewall_status():
    firewall_status = "Enabled" if firewall.is_firewall_enabled() else "Disabled"
    firewall_label.config(text=firewall_status)

def show_network_status():
    network_status = "Connected" if network_check.perform_network_check() else "Disconnected"
    network_status_label.config(text=network_status)

def clear_results():
    system_info_label.config(text="")
    firewall_label.config(text="")
    network_status_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Sanity Check")
window.geometry("400x300")

# Create buttons to trigger the checks
network_button = tk.Button(window, text="Check Network Status", command=show_network_status)
network_button.pack(pady=10)

# Create labels for network check
network_status_label = tk.Label(window, text="Network Check")
network_status_label.pack(pady=10)

# Create buttons to trigger the checks
system_info_button = tk.Button(window, text="Check System Info", command=show_system_info)
system_info_button.pack(pady=10)

# Create labels for system information
system_info_label = tk.Label(window, text="System Information:")
system_info_label.pack(pady=10)

firewall_button = tk.Button(window, text="Check Firewall Status", command=show_firewall_status)
firewall_button.pack(pady=10)

# Create labels for firewall status
firewall_label = tk.Label(window, text="Firewall Status:")
firewall_label.pack(pady=10)

clear_button = tk.Button(window, text="Clear Results", command=clear_results)
clear_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()