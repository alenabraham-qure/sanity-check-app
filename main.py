import platform
import psutil
import ctypes
import os
import tkinter as tk
from tkinter import messagebox

def is_firewall_enabled():
    firewall_state = ctypes.c_long()
    ctypes.windll.hnetcfg.HNetGetFirewallEnabled(None, ctypes.byref(firewall_state))
    return firewall_state.value == 1

def get_system_bit():
    return platform.architecture()[0]

def get_total_ram():
    return psutil.virtual_memory().total

def get_total_storage():
    total, _, _ = psutil.disk_usage('/')
    return total

def is_antivirus_present():
    return any(psutil.win_service_get('WinDefend'))

def is_proxy_used():
    return os.environ.get('HTTP_PROXY') or os.environ.get('HTTPS_PROXY')

def run_sanity_check():
    checks = [
        ("Firewall disabled", is_firewall_enabled),
        ("System bit", get_system_bit),
        ("RAM size", get_total_ram),
        ("Storage size", get_total_storage),
        ("Antivirus present", is_antivirus_present),
        ("Proxy used", is_proxy_used)
    ]

    root = tk.Tk()
    root.title("Sanity Check")
    root.geometry("400x300")

    def show_result():
        result = ""
        for check in checks:
            check_name, check_function = check
            result += f"[{'X' if check_function() else ' '}] {check_name}\n"
        messagebox.showinfo("Sanity Check Result", result)

    label = tk.Label(root, text="Sanity Check", font=("Helvetica", 18, "bold"))
    label.pack(pady=20)

    button = tk.Button(root, text="Run Check", command=show_result)
    button.pack(pady=10)

    root.mainloop()

run_sanity_check()
