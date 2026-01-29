#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import time
import os
from datetime import datetime
import subprocess
import threading
from queue import Queue

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    """Czyści ekran terminala"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    """Wyświetla ASCII art banner"""
    banner = f"""
{RED}    ██╗  ██╗{YELLOW}██╗  ██╗{GREEN}████████╗{CYAN}███████╗{BLUE}███████╗{MAGENTA}██╗
{RED}    ██║  ██║{YELLOW}██║ ██╔╝{GREEN}╚══██╔══╝{CYAN}██╔════╝{BLUE}██╔════╝{MAGENTA}██║
{RED}    ███████║{YELLOW}█████╔╝ {GREEN}   ██║   {CYAN}█████╗  {BLUE}█████╗  {MAGENTA}██║
{RED}    ██╔══██║{YELLOW}██╔═██╗ {GREEN}   ██║   {CYAN}██╔══╝  {BLUE}██╔══╝  {MAGENTA}██║
{RED}    ██║  ██║{YELLOW}██║  ██╗{GREEN}   ██║   {CYAN}███████╗{BLUE}███████╗{MAGENTA}███████╗
{RED}    ╚═╝  ╚═╝{YELLOW}╚═╝  ╚═╝{GREEN}   ╚═╝   {CYAN}╚══════╝{BLUE}╚══════╝{MAGENTA}╚══════╝{RESET}

{CYAN}    ╔═══════════════════════════════════════════════════╗
    ║  {WHITE}Advanced Network Reconnaissance Tool v2.0{CYAN}     ║
    ║  {YELLOW}Coded by: HomewreckerXXX{CYAN}                        ║
    ╚═══════════════════════════════════════════════════╝{RESET}
    """
    print(banner)

def loading_animation():
    """Symuluje ładowanie systemu"""
    print(f"\n{GREEN}[{WHITE}+{GREEN}]{YELLOW} Initializing system...{RESET}")
    time.sleep(0.8)

    print(f"{GREEN}[{WHITE}+{GREEN}]{YELLOW} Loading modules...{RESET}")
    time.sleep(0.6)

    print(f"{GREEN}[{WHITE}+{GREEN}]{YELLOW} Checking network interface...{RESET}")
    time.sleep(0.7)

    print(f"{GREEN}[{WHITE}+{GREEN}]{YELLOW} Establishing secure connection...{RESET}")
    time.sleep(0.5)

    print(f"{GREEN}[{WHITE}+{GREEN}]{YELLOW} Loading exploit database...{RESET}")
    time.sleep(0.9)

    print(f"{GREEN}[{WHITE}+{GREEN}]{YELLOW} Bypassing firewall...{RESET}")
    time.sleep(0.6)

    print(f"{GREEN}[{WHITE}+{GREEN}]{GREEN} Access granted!{RESET}\n")
    time.sleep(1)

    print(f"{CYAN}╔═══════════════════════════════════════════════════╗")
    print(f"{CYAN}║  {BOLD}{WHITE}Welcome to HomewreckerXXX Network Tool!{RESET}{CYAN}          ║")
    print(f"{CYAN}╚═══════════════════════════════════════════════════╝{RESET}\n")
    time.sleep(0.5)

def print_menu():
    """Wyświetla główne menu"""
    print(f"\n{YELLOW}╔════════════════════{WHITE} OPCJE {YELLOW}════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}                                                {YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  {GREEN}[1]{RESET} {CYAN}Szczegółowe skanowanie portów{RESET}            {YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  {GREEN}[2]{RESET} {CYAN}Podsłuchiwanie w sieci lokalnej{RESET}          {YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  {GREEN}[3]{RESET} {CYAN}Szybkie skanowanie sieci (ping sweep){RESET}    {YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  {GREEN}[4]{RESET} {CYAN}Wykrywanie systemu operacyjnego{RESET}          {YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  {RED}[0]{RESET} {RED}Wyjście{RESET}                                   {YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}                                                {YELLOW}║{RESET}")
    print(f"{YELLOW}╚════════════════════════════════════════════════╝{RESET}\n")

def port_scanner():
    """Szczegółowe skanowanie portów"""
    clear_screen()
    print_banner()
    print(f"\n{CYAN}═══════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{WHITE}           SZCZEGÓŁOWE SKANOWANIE PORTÓW{RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════{RESET}\n")

    target = input(f"{GREEN}[{WHITE}?{GREEN}]{YELLOW} Podaj adres IP celu: {RESET}")

    try:
        # Resolving hostname
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{RED}[{WHITE}!{RED}]{RED} Błąd: Nie można rozwiązać hosta!{RESET}")
        input(f"\n{YELLOW}Naciśnij ENTER aby kontynuować...{RESET}")
        return

    print(f"\n{GREEN}[{WHITE}+{GREEN}]{CYAN} Cel: {WHITE}{target} ({target_ip}){RESET}")
    print(f"{GREEN}[{WHITE}+{GREEN}]{CYAN} Rozpoczęto: {WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print(f"{CYAN}─────────────────────────────────────────────────────{RESET}\n")

    # Popularne porty do skanowania
    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
        3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
        8080: "HTTP-Proxy", 8443: "HTTPS-Alt", 27017: "MongoDB"
    }

    choice = input(f"{GREEN}[{WHITE}?{GREEN}]{YELLOW} Skanować [1] Popularne porty  [2] Zakres portów: {RESET}")

    if choice == "1":
        ports_to_scan = list(common_ports.keys())
    else:
        try:
            start = int(input(f"{GREEN}[{WHITE}?{GREEN}]{YELLOW} Port początkowy: {RESET}"))
            end = int(input(f"{GREEN}[{WHITE}?{GREEN}]{YELLOW} Port końcowy: {RESET}"))
            ports_to_scan = range(start, end + 1)
        except ValueError:
            print(f"{RED}[{WHITE}!{RED}]{RED} Błędny zakres portów!{RESET}")
            input(f"\n{YELLOW}Naciśnij ENTER aby kontynuować...{RESET}")
            return

    open_ports = []

    print(f"\n{YELLOW}[{WHITE}~{YELLOW}]{CYAN} Skanowanie w toku...{RESET}\n")

    # Threading dla szybszego skanowania
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                service = common_ports.get(port, "Unknown")
                print(f"{GREEN}[{WHITE}✓{GREEN}]{WHITE} Port {YELLOW}{port:5d}{WHITE} │ {GREEN}OPEN{WHITE}     │ {CYAN}{service}{RESET}")
                open_ports.append((port, service))

            sock.close()
        except:
            pass

    threads = []
    for port in ports_to_scan:
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

        # Limitujemy liczbę równoczesnych wątków
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    # Czekamy na zakończenie pozostałych wątków
    for t in threads:
        t.join()

    print(f"\n{CYAN}═══════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}[{WHITE}✓{GREEN}]{WHITE} Skanowanie zakończone!{RESET}")
    print(f"{GREEN}[{WHITE}+{GREEN}]{CYAN} Znaleziono otwartych portów: {WHITE}{len(open_ports)}{RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════{RESET}")

    input(f"\n{YELLOW}Naciśnij ENTER aby wrócić do menu...{RESET}")

def network_sniffer():
    """Podsłuchiwanie w sieci lokalnej"""
    clear_screen()
    print_banner()
    print(f"\n{CYAN}═══════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{WHITE}      PODSŁUCHIWANIE W SIECI LOKALNEJ (ARP){RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════{RESET}\n")

    print(f"{YELLOW}[{WHITE}!{YELLOW}]{CYAN} Ta funkcja wymaga uprawnień root!{RESET}")

    # Sprawdzamy czy jesteśmy rootem
    if os.geteuid() != 0:
        print(f"{RED}[{WHITE}!{RED}]{RED} Brak uprawnień root! Uruchom jako sudo.{RESET}")
        input(f"\n{YELLOW}Naciśnij ENTER aby wrócić do menu...{RESET}")
        return

    print(f"\n{GREEN}[{WHITE}+{GREEN}]{CYAN} Wykrywanie interfejsów sieciowych...{RESET}\n")

    try:
        # Pobieramy listę interfejsów
        result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True)
        print(result.stdout)

        interface = input(f"\n{GREEN}[{WHITE}?{GREEN}]{YELLOW} Podaj nazwę interfejsu (np. eth0, wlan0): {RESET}")

        print(f"\n{GREEN}[{WHITE}+{GREEN}]{CYAN} Rozpoczynanie nasłuchiwania na {WHITE}{interface}{CYAN}...{RESET}")
        print(f"{YELLOW}[{WHITE}!{YELLOW}]{CYAN} Naciśnij Ctrl+C aby zatrzymać{RESET}\n")
        print(f"{CYAN}─────────────────────────────────────────────────────{RESET}\n")

        time.sleep(1)

        # Uruchamiamy tcpdump lub tshark
        try:
            subprocess.run(['tcpdump', '-i', interface, '-n', '-c', '50'])
        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}[{WHITE}!{YELLOW}]{CYAN} Zatrzymano nasłuchiwanie{RESET}")
        except FileNotFoundError:
            print(f"{RED}[{WHITE}!{RED}]{RED} Narzędzie tcpdump nie jest zainstalowane!{RESET}")
            print(f"{YELLOW}[{WHITE}*{YELLOW}]{CYAN} Zainstaluj: sudo apt install tcpdump{RESET}")

    except Exception as e:
        print(f"{RED}[{WHITE}!{RED}]{RED} Błąd: {e}{RESET}")

    input(f"\n{YELLOW}Naciśnij ENTER aby wrócić do menu...{RESET}")

def ping_sweep():
    """Szybkie skanowanie sieci"""
    clear_screen()
    print_banner()
    print(f"\n{CYAN}═══════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{WHITE}         SZYBKIE SKANOWANIE SIECI (PING SWEEP){RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════{RESET}\n")

    network = input(f"{GREEN}[{WHITE}?{GREEN}]{YELLOW} Podaj sieć (np. 192.168.1): {RESET}")

    print(f"\n{GREEN}[{WHITE}+{GREEN}]{CYAN} Skanowanie sieci {WHITE}{network}.0/24{CYAN}...{RESET}\n")
    print(f"{CYAN}─────────────────────────────────────────────────────{RESET}\n")

    active_hosts = []

    def ping_host(ip):
        try:
            result = subprocess.run(
                ['ping', '-c', '1', '-W', '1', ip],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"{GREEN}[{WHITE}✓{GREEN}]{WHITE} Host {YELLOW}{ip:15s}{WHITE} │ {GREEN}ONLINE{RESET}")
                active_hosts.append(ip)
        except:
            pass

    threads = []
    for i in range(1, 255):
        ip = f"{network}.{i}"
        thread = threading.Thread(target=ping_host, args=(ip,))
        threads.append(thread)
        thread.start()

        if len(threads) >= 50:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print(f"\n{CYAN}═══════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}[{WHITE}✓{GREEN}]{WHITE} Znaleziono aktywnych hostów: {YELLOW}{len(active_hosts)}{RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════{RESET}")

    input(f"\n{YELLOW}Naciśnij ENTER aby wrócić do menu...{RESET}")

def os_detection():
    """Wykrywanie systemu operacyjnego"""
    clear_screen()
    print_banner()
    print(f"\n{CYAN}═══════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{WHITE}       WYKRYWANIE SYSTEMU OPERACYJNEGO (TTL){RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════{RESET}\n")

    target = input(f"{GREEN}[{WHITE}?{GREEN}]{YELLOW} Podaj adres IP celu: {RESET}")

    print(f"\n{GREEN}[{WHITE}+{GREEN}]{CYAN} Wysyłanie pakietów ICMP...{RESET}\n")

    try:
        result = subprocess.run(
            ['ping', '-c', '3', target],
            capture_output=True,
            text=True
        )

        # Analiza TTL
        if 'ttl=' in result.stdout.lower():
            ttl_line = [line for line in result.stdout.split('\n') if 'ttl=' in line.lower()][0]
            ttl = int(ttl_line.split('ttl=')[1].split()[0])

            print(f"{CYAN}─────────────────────────────────────────────────────{RESET}")
            print(f"{GREEN}[{WHITE}+{GREEN}]{WHITE} Wykryto TTL: {YELLOW}{ttl}{RESET}\n")

            # Określanie OS na podstawie TTL
            if ttl <= 64:
                os_guess = "Linux/Unix"
                color = CYAN
            elif ttl <= 128:
                os_guess = "Windows"
                color = BLUE
            else:
                os_guess = "Cisco/Network Device"
                color = MAGENTA

            print(f"{GREEN}[{WHITE}✓{GREEN}]{WHITE} Prawdopodobny system: {color}{os_guess}{RESET}")
            print(f"{CYAN}─────────────────────────────────────────────────────{RESET}")

            print(f"\n{YELLOW}[{WHITE}*{YELLOW}]{CYAN} Legenda TTL:{RESET}")
            print(f"  {CYAN}• 64 lub mniej  → Linux/Unix{RESET}")
            print(f"  {BLUE}• 65-128        → Windows{RESET}")
            print(f"  {MAGENTA}• 129-255      → Urządzenia sieciowe{RESET}")
        else:
            print(f"{RED}[{WHITE}!{RED}]{RED} Nie udało się określić TTL{RESET}")

    except Exception as e:
        print(f"{RED}[{WHITE}!{RED}]{RED} Błąd: {e}{RESET}")

    input(f"\n{YELLOW}Naciśnij ENTER aby wrócić do menu...{RESET}")

def main():
    """Główna funkcja programu"""
    try:
        clear_screen()
        print_banner()
        loading_animation()

        while True:
            print_menu()
            choice = input(f"{GREEN}[{WHITE}>{GREEN}]{YELLOW} Wybierz opcję: {RESET}")

            if choice == "1":
                port_scanner()
            elif choice == "2":
                network_sniffer()
            elif choice == "3":
                ping_sweep()
            elif choice == "4":
                os_detection()
            elif choice == "0":
                print(f"\n{RED}[{WHITE}!{RED}]{CYAN} Zamykanie systemu...{RESET}")
                time.sleep(1)
                print(f"{GREEN}[{WHITE}✓{GREEN}]{GREEN} Do zobaczenia!{RESET}\n")
                sys.exit(0)
            else:
                print(f"{RED}[{WHITE}!{RED}]{RED} Nieprawidłowa opcja!{RESET}")
                time.sleep(1)

            clear_screen()
            print_banner()

    except KeyboardInterrupt:
        print(f"\n\n{RED}[{WHITE}!{RED}]{CYAN} Przerwano przez użytkownika{RESET}")
        print(f"{GREEN}[{WHITE}✓{GREEN}]{GREEN} Do zobaczenia!{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
