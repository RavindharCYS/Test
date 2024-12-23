import nmap

class Scanning:
    def start_scan(self, target):
        try:
            print(f"Starting scan on {target}...")

            # Initialize the PortScanner
            nm = nmap.PortScanner()

            # Scan target for ports in the range 1-1024
            print("Scanning ports 1-1024...")
            nm.scan(target, '1-1024', '-v')

            # Iterate through all detected hosts
            for host in nm.all_hosts():
                print("\n--------------------------------")
                print(f"Host: {host} ({nm[host].hostname()})")
                print(f"State: {nm[host].state()}")

                # Iterate through all protocols for the host
                for proto in nm[host].all_protocols():
                    print(f"\nProtocol: {proto}")
                    
                    # Get list of ports for the protocol
                    ports = sorted(nm[host][proto].keys())
                    for port in ports:
                        port_state = nm[host][proto][port]['state']
                        service = nm[host][proto][port].get('name', 'unknown')
                        print(f"Port: {port}\tState: {port_state}\tService: {service}")

        except Exception as e:
            print(f"Error during scanning: {e}")

if __name__ == "__main__":
    target = input("Enter the target IP or hostname: ")
    scanner = Scanning()
    scanner.start_scan(target)