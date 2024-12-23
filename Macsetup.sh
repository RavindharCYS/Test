#!/bin/bash

# Author: Your Name
# Description: Script to set up the PenTest Tool environment on macOS

echo "=============================="
echo "Setting Up PenTest Tool on macOS"
echo "=============================="

# Function to check if a command is available
command_exists() {
    command -v "$1" &>/dev/null
}

# Step 1: Check for Homebrew installation
echo "Checking for Homebrew..."
if ! command_exists brew; then
    echo "Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

# Step 2: Update Homebrew
echo "Updating Homebrew..."
brew update

# Step 3: Check for Python 3 installation
echo "Checking for Python 3 installation..."
if ! command_exists python3; then
    echo "Python 3 is not installed. Installing Python 3..."
    brew install python3
else
    echo "Python 3 is already installed."
fi

# Step 4: Check for pip installation and upgrade it
echo "Checking for pip installation..."
if ! command_exists pip3; then
    echo "pip is not installed. Installing pip..."
    python3 -m ensurepip --upgrade
else
    echo "pip is already installed. Upgrading pip..."
    python3 -m pip install --upgrade pip
fi

# Step 5: Install required Python libraries
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
pip3 install -r $REQUIREMENTS_FILE

# Step 6: Check and install Nmap
echo "Checking for Nmap installation..."
if ! command_exists nmap; then
    echo "Nmap is not installed. Installing Nmap..."
    brew install nmap
else
    echo "Nmap is already installed."
fi

# Step 7: Check and install Metasploit
echo "Checking for Metasploit Framework installation..."
if ! command_exists msfconsole; then
    echo "Metasploit Framework is not installed. Installing Metasploit..."
    brew install metasploit
else
    echo "Metasploit Framework is already installed."
fi

# Step 8: Install additional tools (if not installed)
echo "Checking for additional tools (git, curl, wget, vim)..."

for tool in git curl wget vim; do
    if ! command_exists $tool; then
        echo "$tool is not installed. Installing $tool..."
        brew install $tool
    else
        echo "$tool is already installed."
    fi
done

# Step 9: Verify Python library installations
echo "=============================="
echo "Verifying Python library installations..."
python3 -c "import nmap, scapy, requests, fpdf, whois, dns, vulners, msfrpc, bs4, shodan, netaddr, paramiko, yaml; print('All Python packages installed successfully.')"

if [ $? -eq 0 ]; then
    echo "All required Python libraries are installed successfully."
else
    echo "Some Python packages failed to install. Check the error messages above."
    exit 1
fi

# Step 10: Verify Nmap installation
echo "Verifying Nmap installation..."
nmap --version

# Step 11: Verify Metasploit installation
echo "Verifying Metasploit installation..."
msfconsole --version

echo "=============================="
echo "Setup Complete! PenTest Tool is ready to use."
echo "=============================="