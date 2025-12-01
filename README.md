**Idle Scan Implementation**

Author: ShubhamSandip SalunkeDate: November30,2025

Description

This toolperformsa TCP IdleScan (side-channelattack)todeterminethe statusofa TCP port ona
targetmachine without sendinganypackets tothe targetfrom the attacker's real IP address.Itrelies
ona "zombie"host with a predictableIP IDsequence.

Prerequisites
OS: Ubuntu 20.04 (SEED VM Recommended)

Python: 3.8+

Libraries: scapy

Installation

sudo pip3 install scapy

chmod +x idle_scanner.py

Usage

The scriptrequires three arguments: the IPofthe zombie, the IP ofthe target, andthe port toscan.
sudo ./idle_scanner.py <ZOMBIE_IP> <TARGET_IP> <PORT>

Example

Scanningport 22 (SSH)ontarget10.9.0.6 usingzombie 10.9.0.5:
sudo ./idle_scanner.py 10.9.0.5 10.9.0.6 22
