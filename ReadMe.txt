Auto PenTest Tool
Project Overview
This is an automated penetration testing tool built using Python and Tkinter for the graphical user interface (GUI). The tool is designed to automate common penetration testing phases, including:

Reconnaissance: Collect information about the target system (e.g., DNS lookup, WHOIS).
Scanning: Scan for open ports, services, and vulnerabilities (using Nmap).
Vulnerability Assessment: Evaluate the target system for known vulnerabilities (using external APIs).
Exploitation: Run exploitation scripts or integrate with Metasploit.
Reporting: Generate a report summarizing the findings of the penetration test.
Technology Stack
Python: The core programming language for the tool.
Tkinter: For creating the user interface.
Nmap: For network scanning (via the python-nmap library).
Requests: For making HTTP requests (e.g., querying APIs for vulnerability data).
FPDF: For generating PDF reports.
Scapy: For low-level network tasks (optional).
Vulners: API for vulnerability scanning.
Metasploit: Optional for exploitation (requires Metasploit installation).
System Requirements
Python 3.x: Ensure Python 3.x is installed.
Pip: Ensure pip (Python package installer) is installed and updated.
Required Libraries: The tool uses several Python libraries, which will be installed automatically using the autorun.bat script.
Setup Instructions
Install Python 3.x:

Download and install Python 3.x from the official Python website: https://www.python.org/downloads/
Make sure to check the box that says "Add Python to PATH" during installation.
Run autorun.bat Script:

In the project folder, locate the autorun.bat file and double-click to run it.
The script will install all necessary Python packages automatically.
It will check that Python is installed, upgrade pip if necessary, and install the required libraries.
Verify Installation:

After the autorun.bat script runs, verify that all packages were installed by checking the console output. If there were any errors, they will be displayed.
Ensure you have installed Nmap and Metasploit on your machine if you want to use the scanning and exploitation features. You can install Nmap from https://nmap.org/download.html.
How to Use the Tool
Launch the Application:

After running the autorun.bat, open the project folder and locate main.py.
Run main.py (via Python) to launch the Tkinter-based GUI.
Tool Interface:

The tool will open a window with five tabs:
Reconnaissance: Gather information (DNS lookup, WHOIS).
Scanning: Scan ports and services using Nmap.
Vulnerability Assessment: Scan the target for known vulnerabilities.
Exploitation: Run Metasploit exploits or custom scripts (requires Metasploit setup).
Reporting: Generate a PDF report with findings from the penetration test.
Perform a Penetration Test:

Reconnaissance: Enter the target domain or IP and click "Start Recon".
Scanning: Enter the target domain or IP and click "Start Scan" to scan open ports.
Vulnerability Assessment: Enter the target and click "Start Assessment" to query a vulnerability database.
Exploitation: Click "Run Exploit" (you must have Metasploit set up to use this feature).
Reporting: Click "Generate Report" to create a PDF report of the results.
Check the Report:

After running the tests, a PDF report will be generated in the same directory as the script, summarizing the results of the penetration test.
Optional Setup (For Exploitation)
To use the Exploitation tab, you'll need Metasploit installed:

Download and install the Metasploit Framework from https://www.metasploit.com/.
Ensure that the Metasploit service is running (msfrpcd for RPC communication) and accessible from your Python script.
Common Issues & Troubleshooting
Missing Python Packages: If any packages fail to install during the autorun.bat run, ensure that you have an active internet connection and try running the script again.
Nmap or Metasploit Not Installed: Some features (scanning and exploitation) require Nmap or Metasploit. Follow the instructions provided in the setup section to install them.
Permission Issues: If you encounter permission errors, try running autorun.bat or main.py as Administrator (right-click > Run as Administrator).
License & Disclaimer
This tool is for educational and ethical penetration testing purposes only. Ensure that you have explicit permission to test the systems you are targeting. Unauthorized penetration testing is illegal and unethical.

