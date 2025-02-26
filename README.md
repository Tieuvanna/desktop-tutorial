# Solana Wallet Generator & Balance Checker

## 📃 Description
This Python script automatically generates new Solana addresses, checks their balance, and saves wallets with a non-zero balance to the `solana_wallets.txt` file.

## 📝 Features
- Generates random Solana addresses and private keys.
- Checks wallet balance using the Solana JSON-RPC API.
- Automatically saves wallets with a balance > 0 to `solana_wallets.txt`.
- Colored output for better readability.

## 🛠 Requirements
- Python 3.6+
- Installed dependencies (see below)

## ⚙️ Installation & Usage
1. **Clone the repository or download the script**:
   ```bash
   git clone https://github.com/Tieuvanna/solana-wallet-checker
   cd solana-wallet-checker
   ```
2. **Install required libraries**:
   ```bash
   pip install requests pynacl base58 colorama
   ```
3. **Run the script**:
   ```bash
   python script.py
   ```

## 🔄 How It Works?
1. The script creates a new key pair (private + public).
2. The public key is converted into a Solana address.
3. A request is sent to `https://api.mainnet-beta.solana.com` to check the balance.
4. If the balance is greater than 0, the wallet is saved to `solana_wallets.txt`.
5. The script repeats these steps in an infinite loop (with a 2-second interval).

## 📁 Saved Wallet Format
If an address has a balance, it is recorded in `solana_wallets.txt` in the following format:
```
Address: 3nBg2Z...k1T8
Private Key: 5H2pZ...6yF5
Balance: 1000000000 lamports (1 SOL)
----------------------------------------
```

## ⚠️ Warning!
- **The script does not search for "rich" wallets** — each new address is empty until SOL is sent to it.
- **Do not share your private keys!** Anyone with a private key can steal funds from the wallet.
- Use this tool **for educational purposes only**.

## 👨‍💻 Author
**Your Name** – [GitHub](https://github.com/Tieuvanna)

## ✅ License
This project is distributed under the **MIT** license.

