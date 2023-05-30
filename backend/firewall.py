# backend/firewall.py

import subprocess

def is_firewall_enabled():
    try:
        output = subprocess.check_output('netsh advfirewall show allprofiles', shell=True)
        output = output.decode('utf-8')
        return 'Firewall Policy' in output and 'BlockInbound' in output
    except subprocess.CalledProcessError:
        return False