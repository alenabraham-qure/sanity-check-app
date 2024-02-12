# backend/firewall.py

import ctypes

def is_firewall_enabled():
    firewall_state = ctypes.c_long()
    ctypes.windll.hnetcfg.HNetGetFirewallEnabled(None, ctypes.byref(firewall_state))
    return firewall_state.value == 1
