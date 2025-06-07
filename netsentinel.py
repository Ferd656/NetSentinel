from flask import Flask, render_template
import nmap
import socket
import ipaddress

app = Flask(__name__)

def scan_network():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network = ipaddress.ip_network(local_ip + '/24', strict=False)
    nm = nmap.PortScanner()
    nm.scan(hosts=network.with_prefixlen, arguments='-O')
    devices = []
    for host in nm.all_hosts():
        ip = host
        try:
            name = nm[host].hostname() or socket.gethostbyaddr(host)[0]
        except Exception:
            name = "Unknown"
        os = "Unknown"
        if 'osmatch' in nm[host] and nm[host]['osmatch']:
            os = nm[host]['osmatch'][0]['name']
        devices.append({'ip': ip, 'name': name, 'os': os})
    return devices

@app.route('/')
def index():
    return render_template('radar.html')

@app.route('/scan')
def scan():
    devices = scan_network()
    return render_template('mainpage.html', devices=devices)

if __name__ == '__main__':
    import threading
    import time
    import webbrowser

    def open_browser():
        time.sleep(2)
        webbrowser.open('http://127.0.0.1:5000')

    threading.Thread(target=open_browser, daemon=True).start()
    app.run(debug=False)
