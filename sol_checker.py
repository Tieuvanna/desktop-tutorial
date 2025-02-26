
import time
import requests
import base58
import nacl.signing
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

# Solana JSON RPC endpoint (Mainnet)
RPC_URL = "https://api.mainnet-beta.solana.com"

# Output file for saving wallets with balance > 0
WALLET_FILE = "solana_wallets.txt"

def generate_solana_address():
    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    # Encode the public key to get the Solana address
    sol_address = base58.b58encode(verify_key.encode()).decode()

    # Encode the private key in Base58
    solana_private_key = signing_key.encode() + verify_key.encode()
    private_key_base58 = base58.b58encode(solana_private_key).decode()

    return sol_address, private_key_base58

# Function to check balance
def get_solana_balance(address):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [address]
    }
    response = requests.post(RPC_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get("result", {}).get("value", 0)  # Balance in lamports
    else:
        print(Fore.RED + "Error fetching balance:", response.text)
        return None

# Function to save wallet to file
def save_wallet(address, private_key, balance):
    with open(WALLET_FILE, "a") as file:
        file.write(f"Address: {address}\nPrivate Key: {private_key}\nBalance: {balance} lamports\n{'-'*40}\n")
    print(Fore.MAGENTA + f"Wallet saved to {WALLET_FILE}")

# Infinite loop to generate new addresses and check balances
while True:
    sol_address, private_key_base58 = generate_solana_address()

    print(Fore.CYAN + f"\nSolana Address: {sol_address}")
    print(Fore.YELLOW + f"Private Key: {private_key_base58}")

    balance = get_solana_balance(sol_address)
    if balance is not None:
        print(Fore.RED + f"Balance: {balance} ({balance / 1_000_000_000} SOL)")

        # Save wallet if balance is greater than 0
        if balance > 0:
            save_wallet(sol_address, private_key_base58, balance)
    else:
        print(Fore.RED + "Failed to retrieve balance.")

    time.sleep(2)

