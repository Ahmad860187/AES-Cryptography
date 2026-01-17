# ECB (Electronic Codebook) mode - simplest AES mode
# Each block encrypted independently (not secure for multiple blocks!)

from ..aes_block import AESBlock
from ..padding import pad_zero_count,unpad_zero_count

def encrypt(key,pt):
    # Encrypt plaintext using ECB mode
    a=AESBlock(key)
    pt=pad_zero_count(pt,16)  # Pad to multiple of 16 bytes
    out=bytearray()
    # Encrypt each 16-byte block independently
    for i in range(0,len(pt),16):
        out+=a.encrypt_block(pt[i:i+16])
    return bytes(out)

def decrypt(key,ct):
    # Decrypt ciphertext using ECB mode
    a=AESBlock(key)
    out=bytearray()
    # Decrypt each 16-byte block independently
    for i in range(0,len(ct),16):
        out+=a.decrypt_block(ct[i:i+16])
    return unpad_zero_count(bytes(out),16)  # Remove padding
