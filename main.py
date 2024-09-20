import requests
import time
import random
import hashlib
import json
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Membaca konfigurasi dari file config.json
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

# Membaca token otentikasi dari file auth.txt
def load_auth_token():
    with open('auth.txt', 'r') as f:
        return f.read().strip()

# Konfigurasi
config = load_config()
BASE_URL = 'https://api.freedogs.bot/miniapps/api'
AUTH_TOKEN = load_auth_token()
MIN_COINS_REQUIRED = config['MIN_COINS_REQUIRED']
MAX_COLLECT_AMOUNT = config['MAX_COLLECT_AMOUNT']
COLLECT_INTERVAL = config['COLLECT_INTERVAL']
RETRY_INTERVAL = 10  # Waktu tunggu sebelum retry jika gagal

def get_headers():
    return {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

def get_game_data():
    try:
        response = requests.get(f'{BASE_URL}/user_game_level/GetGameInfo', headers=get_headers())
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print_colored(f"Error fetching game data: {e}", Fore.RED)
        return None

def collect_coins(amount, hash_code, collect_seq_no):
    data = {
        'collectAmount': amount,
        'hashCode': hash_code,
        'collectSeqNo': collect_seq_no
    }
    try:
        response = requests.post(f'{BASE_URL}/user_game/collectCoin', headers=get_headers(), data=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print_colored(f"Error collecting coins: {e}", Fore.RED)
        return None

def generate_hash_code(collect_amount, collect_seq_no):
    data = f"{collect_amount}{collect_seq_no}7be2a16a82054ee58398c5edb7ac4a5a"
    return hashlib.md5(data.encode()).hexdigest()

def print_colored(message, color):
    print(f"{color}{message}{Style.RESET_ALL}")

def main():
    while True:
        # Ambil data game
        game_data = get_game_data()
        if game_data is None or game_data.get('code') != 0:
            print_colored("Failed to fetch game data. Retrying...", Fore.RED)
            time.sleep(RETRY_INTERVAL)
            continue
        
        print_colored("Game data fetched successfully.", Fore.GREEN)
        coin_pool_left = int(game_data['data']['coinPoolLeft'])
        collect_seq_no = int(game_data['data']['collectSeqNo'])
        
        # Update jumlah koin lokal
        local_collect_amount = random.randint(1, MAX_COLLECT_AMOUNT)
        print_colored(f"Local collect amount updated to: {local_collect_amount}", Fore.CYAN)

        # Cek jika sisa koin sesuai dengan minimal yang diinginkan
        if coin_pool_left >= MIN_COINS_REQUIRED:
            collect_amount = random.randint(1, local_collect_amount)  # Koleksi koin dengan jumlah acak
            hash_code = generate_hash_code(collect_amount, collect_seq_no)
            print_colored(f"Collecting coins, amount: {collect_amount}", Fore.YELLOW)
            
            # Kirim permintaan koleksi koin
            result = collect_coins(collect_amount, hash_code, collect_seq_no)
            if result is None:
                print_colored("Error during coin collection. Retrying...", Fore.RED)
                time.sleep(RETRY_INTERVAL)
                continue

            if result['code'] == 0 and result['data']['collectStatus']:
                collect_seq_no = int(result['data']['collectSeqNo'])
                print_colored(f"Coins collected successfully! Total gold coins: {collect_amount}", Fore.GREEN)
            else:
                print_colored("Failed to collect coins.", Fore.RED)

        else:
            print_colored(f"Not enough coins available to collect. Coins left: {coin_pool_left}", Fore.RED)

        # Tunggu sebelum koleksi berikutnya
        print_colored(f"Waiting for {COLLECT_INTERVAL} seconds before next collection...", Fore.MAGENTA)
        time.sleep(COLLECT_INTERVAL)

def print_title():
    title = f"""
{Fore.GREEN}=============================
=     {Fore.YELLOW}FREEDOG AUTO COLLECT{Fore.GREEN}  =
=============================
= {Fore.CYAN}Channel : {Fore.LIGHTBLUE_EX}t.me/ugdairdrop{Fore.GREEN} =
============================={Style.RESET_ALL}
"""
    print(title)

# Panggil fungsi print_title di bagian awal program
if __name__ == '__main__':
    print_title()
    try:
        main()
    except KeyboardInterrupt:
        print_colored("Program stopped by user.", Fore.YELLOW)
