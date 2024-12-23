@echo off
title Auto PenTest Tool Setup
echo =========================================
echo       Setting Up PenTest Tool
echo =========================================

:: Step 1: Check Python Installation
echo Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3 and ensure it is added to the PATH.
    pause
    exit /b
) else (
    echo Python is already installed.
)

:: Step 2: Check pip Installation
echo Checking for pip installation...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
) else (
    echo pip is already installed. Upgrading pip...
    python -m pip install --upgrade pip
)

:: Step 3: Install Required Python Libraries
echo Installing required Python libraries...
if not exist requirements.txt (
    echo requirements.txt not found. Creating a default requirements.txt...
    echo python-nmap > requirements.txt
    echo scapy >> requirements.txt
    echo requests >> requirements.txt
    echo fpdf >> requirements.txt
    echo whois >> requirements.txt
    echo dnspython >> requirements.txt
    echo vulners >> requirements.txt
    echo msfrpc >> requirements.txt
    echo beautifulsoup4 >> requirements.txt
    echo shodan >> requirements.txt
    echo netaddr >> requirements.txt
    echo paramiko >> requirements.txt
    echo pyyaml >> requirements.txt
)

pip install -r requirements.txt

:: Step 4: Check for Nmap Installation
echo Checking for Nmap installation...
where nmap >nul 2>&1
if %errorlevel% neq 0 (
    echo Nmap is not installed. Downloading and installing Nmap...
    powershell -Command "& {Invoke-WebRequest -Uri https://nmap.org/dist/nmap-7.94-setup.exe -OutFile nmap-setup.exe}"
    echo Installing Nmap...
    start /wait "" nmap-setup.exe /S
    del nmap-setup.exe
) else (
    echo Nmap is already installed.
)

:: Step 5: Check for Metasploit Installation
echo Checking for Metasploit installation...
where msfconsole >nul 2>&1
if %errorlevel% neq 0 (
    echo Metasploit Framework is not installed.
    echo Please download Metasploit for Windows from https://metasploit.com/ and install it manually.
    echo Ensure msfconsole is added to the PATH.
) else (
    echo Metasploit Framework is already installed.
)

:: Step 6: Verify Python Libraries
echo =========================================
echo Verifying Python library installations...
python -c "import nmap, scapy, requests, fpdf, whois, dns, vulners, bs4, shodan, netaddr, paramiko, yaml; print('All Python libraries are installed successfully.')"
if %errorlevel% neq 0 (
    echo Some Python libraries failed to install. Please check the errors above.
    pause
    exit /b
) else (
    echo All Python libraries installed successfully.
)

:: Step 7: Final Verification
echo =========================================
echo Verifying Nmap installation...
nmap --version
echo =========================================
echo If you have installed Metasploit, verify using msfconsole --version
echo =========================================
echo Setup Complete! Your PenTest Tool is ready to use.
pause
exit