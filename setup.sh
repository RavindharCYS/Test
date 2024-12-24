#!/bin/bash

# Author: Ravindhar V
# Description: Script to set up the PenTest Tool environment on Linux (Ubuntu/Debian)

echo "=============================="
echo "Setting Up PenTest Tool"
echo "=============================="

# Function to check if a package is installed
is_installed() {
    dpkg -l | grep -q "^ii  $1 "
}

# Step 1: Update system packages
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Step 2: Check for Python 3 installation
echo "Checking for Python 3 installation..."
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing Python 3..."
    sudo apt install -y python3 python3-pip python3-dev
else
    echo "Python 3 is already installed."
fi

# Step 3: Check for pip installation and upgrade it
echo "Checking for pip installation..."
if ! command -v pip3 &>/dev/null; then
    echo "pip is not installed. Installing pip..."
    sudo apt install -y python3-pip
else
    echo "pip is already installed. Upgrading pip..."
    python3 -m pip install --upgrade pip
fi

# Step 4: Install required Python libraries
REQUIREMENTS_FILE="requirements.txt"

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "requirements.txt not found. Creating a default requirements.txt file..."

    cat <<EOL > $REQUIREMENTS_FILE
python-nmap
scapy
requests
fpdf
whois
dnspython
vulners
msfrpc
beautifulsoup4
shodan
netaddr
paramiko
pyyaml
EOL
fi

echo "Installing Python dependencies..."
python3 -m pip install -r $REQUIREMENTS_FILE

# Step 5: Check and install Nmap
echo "Checking for Nmap installation..."
if ! command -v nmap &>/dev/null; then
    echo "Nmap is not installed. Installing Nmap..."
    sudo apt install -y nmap
else
    echo "Nmap is already installed."
fi

# Step 6: Check and install Metasploit Framework
echo "Checking for Metasploit Framework installation..."
if ! command -v msfconsole &>/dev/null; then
    echo "Metasploit Framework is not installed. Installing Metasploit..."
    sudo apt install -y metasploit-framework
else
    echo "Metasploit Framework is already installed."
fi

# Step 7: Install additional tools (if not installed)
echo "Checking for additional tools (git, curl, wget, vim)..."

for tool in git curl wget vim; do
    if ! command -v $tool &>/dev/null; then
        echo "$tool is not installed. Installing $tool..."
        sudo apt install -y $tool
    else
        echo "$tool is already installed."
    fi
done

# Step 8: Verify Python library installations
echo "=============================="
echo "Verifying Python library installations..."
python3 -c "import nmap, scapy, requests, fpdf, whois, dns, vulners, msfrpc, bs4, shodan, netaddr, paramiko, yaml; print('All Python packages installed successfully.')"

if [ $? -eq 0 ]; then
    echo "All required Python libraries are installed successfully."
else
    echo "Some Python packages failed to install. Check the error messages above."
    exit 1
fi

# Step 9: Verify Nmap installation
echo "Verifying Nmap installation..."
nmap --version

# Step 10: Verify Metasploit installation
echo "Verifying Metasploit installation..."
msfconsole --version

echo "=============================="
echo "Setup Complete!"
echo "=============================="
