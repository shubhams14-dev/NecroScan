**Idle Scan Implementation**

**Author**: Shubham Sandip Salunke Date: November 30,2025

**Description**

This tool performs a TCP IdleScan (side-channelattack)todeterminethe status of a TCP port on a
target machine without sending any packets to the target from the attacker's real IP address.It relies
on a "zombie" host with a predictable IP ID sequence.

**Prerequisites**
OS: Ubuntu 20.04 (SEED VM Recommended)

Python: 3.8+

**Libraries**: scapy

**Installation**

sudo pip3 install scapy

chmod +x idle_scanner.py

**Usage**

The script requires three arguments: the IP of the zombie, the IP of the target, and the port to scan.
sudo ./idle_scanner.py <ZOMBIE_IP> <TARGET_IP> <PORT>

**Example**

Scanning port 22 (SSH)on target 10.9.0.6 using zombie 10.9.0.5:
sudo ./idle_scanner.py 10.9.0.5 10.9.0.6 22
