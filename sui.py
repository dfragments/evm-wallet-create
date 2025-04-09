import secrets
import nacl.signing
import base64

def generate_sui_private_key():
    seed = secrets.token_bytes(32)
    private_key_base64 = base64.b64encode(seed).decode("utf-8")
    return private_key_base64

def save_wallets_to_file(filename, count):
    with open(filename, "w") as f:
        for _ in range(count):
            private_key = generate_sui_private_key()
            f.write(f"{private_key}\n")
    print(f"{count} Sui private keys generated and saved to {filename}")

if __name__ == "__main__":
    num_wallets = int(input("Enter number of wallets to generate: "))
    save_wallets_to_file("wallets.txt", num_wallets)
#pip install pynacl
