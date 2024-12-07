import requests
import json
import sys
import socket
from bs4 import BeautifulSoup
from colorama import Fore, Style

def print_main_menu():
    ascii_art = r"""



________  ._____________  _____       _____   ____ ___.____  ___________.___        ___________________   ________  .____       _________
\______ \ |   \______   \/  _  \     /     \ |    |   \    | \__    ___/|   |       \__    ___/\_____  \  \_____  \ |    |     /   _____/
 |    |  \|   ||     ___/  /_\  \   /  \ /  \|    |   /    |   |    |   |   |  ______ |    |    /   |   \  /   |   \|    |     \_____  \ 
 |    `   \   ||    |  /    |    \ /    Y    \    |  /|    |___|    |   |   | /_____/ |    |   /    |    \/    |    \    |___  /        \
/_______  /___||____|  \____|__  / \____|__  /______/ |_______ \____|   |___|         |____|   \_______  /\_______  /_______ \/_______  /
        \/                     \/          \/                 \/                                       \/         \/        \/        \/ 



DIPA MULTI-TOOLS

    """
    print(ascii_art)
    print("===== PILIHAN MENU =====")
    print("1. IP Tracker")
    print("2. Page Scanner")
    print("3. Subdomain Finder")
    print("4. IP Scanner")
    print("5. Keluar")

def ip_tracker():
    ascii_art = r"""


________  .__               .___         ___________                     __                  
\______ \ |__|__________    |   |_____   \__    ___/___________    ____ |  | __ ___________ 
 |    |  \|  \____ \__  \   |   \____ \    |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
 |    `   \  |  |_> > __ \_ |   |  |_> >   |    |   |  | \// __ \\  \___|    <\  ___/|  | \/
 /_______  /__|   __(____  / |___|   __/    |____|   |__|  (____  /\___  >__|_ \\___  >__|   
        \/   |__|       \/      |__|                           \/     \/     \/    \/        

    """
    print(ascii_art)

    def get_ip_info(ip):
        access_key = '864d8029bb8923'  # Ganti dengan API key kamu dari ipinfo.io
        url = f'http://ipinfo.io/{ip}/json?token={access_key}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print("Gagal mendapatkan informasi IP. Periksa kembali alamat IP atau API key.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan koneksi: {e}")
            return None

    ip = input("Masukkan alamat IP yang ingin dilacak: ").strip()
    if not ip:
        ip = 'me'

    print("\nMelacak informasi untuk IP:", ip)
    ip_info = get_ip_info(ip)
    if ip_info:
        print("\nInformasi IP:")
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname', 'Tidak tersedia')}")
        print(f"Kota: {ip_info.get('city', 'Tidak tersedia')}")
        print(f"Region: {ip_info.get('region', 'Tidak tersedia')}")
        print(f"Negara: {ip_info.get('country', 'Tidak tersedia')}")
        print(f"Lokasi: {ip_info.get('loc', 'Tidak tersedia')}")
        print(f"Organisasi: {ip_info.get('org', 'Tidak tersedia')}")
    else:
        print("Tidak ada data untuk IP tersebut.")

def page_scanner():
    ascii_art = r"""

________  .__               __________                         _________                     
\______ \ |__|__________    \______   \_____     ____   ____  /   _____/ ____ _____    ____  
 |    |  \|  \____ \__  \    |     ___/\__  \   / ___\_/ __ \ \_____  \_/ ___\\__  \  /    \ 
 |    `   \  |  |_> > __ \_  |    |     / __ \_/ /_/  >  ___/ /        \  \___ / __ \|   |  \
/_______  /__|   __(____  /  |____|    (____  /\___  / \___  >_______  /\___  >____  /___|  /
        \/   |__|       \/                  \/_____/      \/        \/     \/     \/     \/ 

    """
    print(ascii_art)

    def scan_page(url):
        try:
            print(f"\nMenganalisis URL: {url}...")
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"\n[INFO] Status Kode: {response.status_code}")
            print(f"[INFO] Judul Halaman: {soup.title.string if soup.title else 'Tidak ada judul'}")
            print("\n[INFO] Daftar Link yang Ditemukan:")
            links = soup.find_all('a', href=True)
            for idx, link in enumerate(links, 1):
                print(f"{idx}. {link['href']}")
        except requests.exceptions.RequestException as e:
            print(f"\n[ERROR] Terjadi kesalahan saat mengakses halaman: {e}")

    url = input("Masukkan URL untuk di-scan (gunakan https): ").strip()
    scan_page(url)

def ip_scanner():
    ascii_art = r"""
________  ._____________  _____    ._____________    __________________     _____    _______    _______  _____________________ 
\______ \ |   \______   \/  _  \   |   \______   \  /   _____/\_   ___ \   /  _  \   \      \   \      \ \_   _____/\______   \
 |    |  \|   ||     ___/  /_\  \  |   ||     ___/  \_____  \ /    \  \/  /  /_\  \  /   |   \  /   |   \ |    __)_  |       _/
 |    `   \   ||    |  /    |    \ |   ||    |      /        \\     \____/    |    \/    |    \/    |    \|        \ |    |   \
/_______  /___||____|  \____|__  / |___||____|     /_______  / \______  /\____|__  /\____|__  /\____|__  /_______  / |____|_  /
        \/                     \/                          \/         \/         \/         \/         \/        \/         \/  
    """
    print(ascii_art)

    def check_domain(domain):
        try:
            ip = socket.gethostbyname(domain)
            print(f"[INFO] {domain} resolved to {ip}")
        except socket.gaierror:
            print(f"[ERROR] Unable to resolve domain: {domain}")
            return False

        try:
            response = requests.get(f"http://{domain}", timeout=5)
            print(f"[INFO] {domain} is active with status code {response.status_code}")
            return True
        except requests.RequestException as e:
            print(f"[ERROR] Unable to connect to {domain}: {e}")
            return False

    domains = input("Enter domains to scan (comma-separated): ").split(",")
    domains = [domain.strip() for domain in domains]

    print("\nScanning domains...\n")
    for domain in domains:
        check_domain(domain)

    print("\nScan complete.")

def dipa_tools():
    ascii_art = r"""

     ____    _   ____
    |  _ \  | | |  __\    /\                                     
    | | | | | | | |__)   //\\
    | |_| | | | |  __/  / __ \
    |____/  |_| |_|    /_/  \_\
                                                 
    """
    print(ascii_art)
    print(f"{Fore.YELLOW}[ INF ] Silakan Isi.")

    def get_subdomains(domain):
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            subdomains = set()
            for entry in data:
                subdomain = entry['name_value']
                subdomains.add(subdomain)
            return subdomains
        except requests.exceptions.RequestException:
            print(f"{Fore.RED}[ ERR ] Error fetching data")
            return set()

    domain = input("Masukkan domain yang ingin dicari subdomainnya: ").strip()
    subdomains = get_subdomains(domain)

    if subdomains:
        print(f"{Fore.GREEN}Subdomains ditemukan untuk {domain}:\n")
        for idx, subdomain in enumerate(sorted(subdomains), start=1):
            print(f"{Fore.WHITE}[ {idx} ] {subdomain}")
    else:
        print(f"{Fore.WHITE}[ ERR ] Tidak ditemukan subdomain untuk {domain}.")

def main():
    while True:
        print_main_menu()
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            ip_tracker()
        elif pilihan == "2":
            page_scanner()
        elif pilihan == "3":
            dipa_tools()
        elif pilihan == "4":
            ip_scanner()
        elif pilihan == "5":
            print("Keluar dari program. Terima kasih telah menggunakan DIPA Multi-Tools!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
