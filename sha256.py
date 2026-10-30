import hashlib

def sha256_hex(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def unterschiedliche_bits(hex1, hex2):
    return bin(int(hex1, 16) ^ int(hex2, 16)).count("1")

print(sha256_hex("Papier593102"))
