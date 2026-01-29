#!/bin/bash

# HKTOOL Installation Script
# Auto-detects Linux distribution and installs dependencies

RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
RESET='\033[0m'

echo -e "${CYAN}═══════════════════════════════════════════════════════${RESET}"
echo -e "${CYAN}      HKTOOL v3.0 - Automatic Installation Script${RESET}"
echo -e "${CYAN}═══════════════════════════════════════════════════════${RESET}\n"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}[!] This script must be run as root!${RESET}"
    echo -e "${YELLOW}[*] Please run: sudo bash install.sh${RESET}\n"
    exit 1
fi

echo -e "${GREEN}[+]${RESET} Detecting Linux distribution..."

# Detect distribution
if [ -f /etc/debian_version ]; then
    DISTRO="debian"
    echo -e "${GREEN}[+]${RESET} Detected: Debian/Ubuntu/Kali/Parrot"
    PKG_MANAGER="apt"
    UPDATE_CMD="apt update"
    INSTALL_CMD="apt install -y"
elif [ -f /etc/redhat-release ]; then
    DISTRO="redhat"
    echo -e "${GREEN}[+]${RESET} Detected: RedHat/CentOS/Fedora"
    PKG_MANAGER="yum"
    UPDATE_CMD="yum update -y"
    INSTALL_CMD="yum install -y"
elif [ -f /etc/arch-release ]; then
    DISTRO="arch"
    echo -e "${GREEN}[+]${RESET} Detected: Arch Linux"
    PKG_MANAGER="pacman"
    UPDATE_CMD="pacman -Syu --noconfirm"
    INSTALL_CMD="pacman -S --noconfirm"
elif [ -f /etc/fedora-release ]; then
    DISTRO="fedora"
    echo -e "${GREEN}[+]${RESET} Detected: Fedora"
    PKG_MANAGER="dnf"
    UPDATE_CMD="dnf update -y"
    INSTALL_CMD="dnf install -y"
else
    echo -e "${YELLOW}[!]${RESET} Unknown distribution. Trying apt..."
    DISTRO="unknown"
    PKG_MANAGER="apt"
    UPDATE_CMD="apt update"
    INSTALL_CMD="apt install -y"
fi

echo -e "\n${YELLOW}[*]${RESET} Updating package manager..."
$UPDATE_CMD

echo -e "\n${GREEN}[+]${RESET} Installing Python dependencies..."
$INSTALL_CMD python3 python3-pip

echo -e "\n${GREEN}[+]${RESET} Installing network tools..."

# Install common tools
TOOLS="tcpdump wireshark-common nmap netcat arp-scan net-tools"

if [ "$DISTRO" = "arch" ]; then
    TOOLS="tcpdump wireshark-cli nmap gnu-netcat arp-scan net-tools"
fi

for tool in $TOOLS; do
    echo -e "${CYAN}  [~]${RESET} Installing $tool..."
    $INSTALL_CMD $tool 2>/dev/null
done

# Install tshark separately (might require special handling)
if [ "$DISTRO" = "debian" ]; then
    echo -e "${CYAN}  [~]${RESET} Installing tshark..."
    DEBIAN_FRONTEND=noninteractive $INSTALL_CMD tshark
elif [ "$DISTRO" = "redhat" ] || [ "$DISTRO" = "fedora" ]; then
    echo -e "${CYAN}  [~]${RESET} Installing wireshark..."
    $INSTALL_CMD wireshark
elif [ "$DISTRO" = "arch" ]; then
    echo -e "${CYAN}  [~]${RESET} tshark already included in wireshark-cli"
fi

# Make hktool executable
echo -e "\n${GREEN}[+]${RESET} Setting up HKTOOL..."
chmod +x hktool.py

# Create symlink in /usr/local/bin (optional)
if [ -f "hktool.py" ]; then
    ln -sf "$(pwd)/hktool.py" /usr/local/bin/hktool 2>/dev/null
    echo -e "${GREEN}[+]${RESET} Created symlink: /usr/local/bin/hktool"
fi

echo -e "\n${CYAN}═══════════════════════════════════════════════════════${RESET}"
echo -e "${GREEN}[✓] Installation complete!${RESET}\n"
echo -e "${YELLOW}Usage:${RESET}"
echo -e "  ${GREEN}python3 hktool.py${RESET}           - Main menu"
echo -e "  ${GREEN}python3 hktool.py --console${RESET} - Interactive console"
echo -e "  ${GREEN}python3 hktool.py --help${RESET}    - Show help"
echo -e "  ${GREEN}sudo python3 hktool.py${RESET}      - Run with root privileges\n"
echo -e "${CYAN}═══════════════════════════════════════════════════════${RESET}\n"
