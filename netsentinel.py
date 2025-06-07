import nmap
import socket
import ipaddress

# Get local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Guess the local network (assume /24 subnet)
network = ipaddress.ip_network(local_ip + '/24', strict=False)

print(f"Scanning network: {network}")

nm = nmap.PortScanner()

# Scan the network for live hosts and OS detection
scan_result = nm.scan(hosts=str(network), arguments='-O')

print("\nDevices found:")
print(f"{'IP Address':<16} {'Hostname':<30} {'OS':<30}")
print("-"*80)

for host in nm.all_hosts():
    ip = host
    try:
        name = nm[host].hostname() or socket.gethostbyaddr(host)[0]
    except Exception:
        name = "Unknown"
    os = "Unknown"
    if 'osmatch' in nm[host] and nm[host]['osmatch']:
        os = nm[host]['osmatch'][0]['name']
    print(f"{ip:<16} {name:<30} {os:<30}")
