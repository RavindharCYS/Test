import socket
import whois # type: ignore
import subprocess
from concurrent.futures import ThreadPoolExecutor

class Reconnaissance:
    def start_recon(self, target):
        try:
            print(f"Starting reconnaissance on {target}...")

            # Get the IP address of the target
            ip = socket.gethostbyname(target)
            print(f"IP Address of {target}: {ip}")

            # Perform WHOIS lookup
            self.whois_lookup(target)

            # Perform DNS lookup
            self.dns_lookup(target)

            # Perform port scanning
            self.port_scan(ip)

        except Exception as e:
            print(f"Error during reconnaissance: {e}")

    def whois_lookup(self, target):
        try:
            print("\nPerforming WHOIS lookup...")
            domain_info = whois.whois(target)
            print("WHOIS Information:")
            print(domain_info)
        except Exception as e:
            print(f"Error during WHOIS lookup: {e}")

    def dns_lookup(self, target):
        try:
            print("\nPerforming DNS lookup...")
            dns_records = socket.gethostbyname_ex(target)
            print("DNS Records:")
            print(f"Host Name: {dns_records[0]}")
            print(f"Aliases: {dns_records[1]}")
            print(f"IP Addresses: {dns_records[2]}")
        except Exception as e:
            print(f"Error during DNS lookup: {e}")

    def port_scan(self, ip):
        try:
            print("\nPerforming port scan...")
            common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]
            open_ports = []

            def scan_port(port):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(1)
                        if s.connect_ex((ip, port)) == 0:
                            open_ports.append(port)
                except:
                    pass

            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(scan_port, common_ports)

            if open_ports:
                print(f"Open Ports: {', '.join(map(str, open_ports))}")
            else:
                print("No common ports are open.")

        except Exception as e:
            print(f"Error during port scanning: {e}")

if __name__ == "__main__":
    target = input("Enter the target domain or IP address: ")
    recon = Reconnaissance()
    recon.start_recon(target)
