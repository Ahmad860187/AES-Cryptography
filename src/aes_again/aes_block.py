# AES block cipher wrapper - encrypts/decrypts single 16-byte blocks
from Crypto.Cipher import AES

class AESBlock:
    def __init__(self,key:bytes):
        # Store encryption key (16, 24, or 32 bytes)
        self.key=key
    
    def encrypt_block(self,block16:bytes)->bytes:
        # Encrypt a single 16-byte block using AES-ECB
        return AES.new(self.key,AES.MODE_ECB).encrypt(block16)
    
    def decrypt_block(self,block16:bytes)->bytes:
        # Decrypt a single 16-byte block using AES-ECB
        return AES.new(self.key,AES.MODE_ECB).decrypt(block16)
