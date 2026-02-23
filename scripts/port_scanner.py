"""
Port Scanner Script
Author: Mbali Nene
Description:
    A simple TCP port scanner that checks if a specific port
    is open on a given host.
"""

import socket


def scan_port(host: str, port: int) -> None:
    """
    Attempts to connect to a specified host and port.
    Prints whether the port is open or closed.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            result = s.connect_ex((host, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN on {host}")
            else:
                print(f"[-] Port {port} is CLOSED on {host}")

    except socket.gaierror:
        print("[!] Invalid host. Please check the hostname.")
    except Exception as e:
        print(f"[!] Error occurred: {e}")


def main():
    host = input("Enter target host (e.g., google.com): ")
    port = int(input("Enter port number to scan: "))

    scan_port(host, port)


if __name__ == "__main__":
    main()
