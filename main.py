import os
import hashlib

def generate_eth_address():
    private_key = os.urandom(32).hex()
    public_key = "0x" + hashlib.sha3_256(bytes.fromhex(private_key)).hexdigest()[24:]
    return (private_key, public_key)

private_key, public_key = generate_eth_address()
print("Private key:", private_key)
print("Public key:", public_key)
