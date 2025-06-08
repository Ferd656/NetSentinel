# NetSentinel

NetSentinel is a Python application that uses Nmap to scan your local network and display all connected devices, including their IP addresses, operating systems, and hostnames.

## Requirements
- Python 3.7+
- Nmap installed on your system
- `python-nmap` library

## Setup
1. Install Nmap from https://nmap.org/download.html
2. Install the required Python package:
   ```powershell
   pip install python-nmap
   ```

## Usage
Run the following command in PowerShell:
```powershell
python netsentinel.py
```

## Example
The application will scan your local network and display a list of connected devices with their IP, OS, and Name.

### Scanning process
<img src="sample_images/NetSentinel ScanningProcess.png" alt="Scanning process" style="max-width:600px;height:auto;" />

### Result
<img src="sample_images/NetSentinel Example.png" alt="Scan results view" style="max-width:600px;height:auto;"/>