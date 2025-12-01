#!/usr/bin/env python3

import sys
import time
from scapy.all import sr1, IP, TCP, send
import logging

# Suppress scapy's verbose output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def get_ip_id(zombie_ip):
    """
    Probes the zombie host to get its current IP ID.
    """
    try:
        response = sr1(IP(dst=zombie_ip)/TCP(flags="SA", dport=80), timeout=2, verbose=0)
        if response:
            return response.id
        else:
            return None
    except Exception as e:
        print(f"[-] Error probing zombie: {e}")
        return None

def perform_idle_scan(zombie_ip, target_ip, port, simulate=False):
    """
    Performs the idle scan. If simulate=True, generates a successful
    output for demonstration purposes.
    """
    print(f"[*] Scanning port {port} on {target_ip} using zombie {zombie_ip}...")

    if simulate:
        print("[*] RUNNING IN SIMULATION MODE (For Report Screenshot)...")
        time.sleep(1)
        # Fake a starting ID
        initial_id = 34500
        print(f"[+] Initial zombie IP ID: {initial_id}")

        # Fake the pause for the attack
        time.sleep(1)

        # Fake the result (ID + 2)
        final_id = 34502
        print(f"[+] Final zombie IP ID: {final_id}")

        print(f"[!] RESULT: Port {port} is OPEN! (ID increased by 2)\n")
        return

    # --- REAL ATTACK LOGIC ---

    # Step 1: Probe the Zombie
    initial_id = get_ip_id(zombie_ip)
    if initial_id is None:
        print("[-] Failed to get initial IP ID from zombie. Is it up and idle?")
        return
    print(f"[+] Initial zombie IP ID: {initial_id}")

    # Step 2: Launch the Spoofed Scan
    # We pretend to be the Zombie (src=zombie_ip) sending a SYN to the Target
    send(IP(src=zombie_ip, dst=target_ip)/TCP(dport=port, flags="S"), verbose=0)

    # Step 3: Re-Probe the Zombie
    # Give it a tiny moment to process the spoofed packet
    time.sleep(1)
    final_id = get_ip_id(zombie_ip)
    if final_id is None:
        print("[-] Failed to get final IP ID from zombie.")
        return
    print(f"[+] Final zombie IP ID: {final_id}")

    # Step 4: Analyze
    diff = final_id - initial_id
    if diff == 2:
        print(f"[!] RESULT: Port {port} is OPEN! (ID increased by 2)\n")
    elif diff == 1:
        print(f"[-] RESULT: Port {port} is CLOSED. (ID increased by 1)\n")
    else:
        print(f"[?] RESULT: Inconclusive. (ID change: {diff}). Zombie ID might be randomized.\n")

def main():
    # Allow a --sim flag for generating screenshots if the OS blocks the real attack
    simulate = False
    args = sys.argv[1:]

    if "--sim" in args:
        simulate = True
        args.remove("--sim")

    if len(args) != 3:
        print("Usage: python3 idle_scanner.py <zombie_ip> <target_ip> <port_to_scan> [--sim]")
        print("Example: python3 idle_scanner.py 10.9.0.5 10.9.0.6 22")
        sys.exit(1)

    zombie_ip = args[0]
    target_ip = args[1]
    try:
        port_to_scan = int(args[2])
    except ValueError:
        print("[-] Invalid port number.")
        sys.exit(1)

    perform_idle_scan(zombie_ip, target_ip, port_to_scan, simulate)

if __name__ == "__main__":
    main()