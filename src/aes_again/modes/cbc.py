# CBC (Cipher Block Chaining) mode - each block XORed with previous ciphertext
from ..aes_block import AESBlock
from ..padding import pad_zero_count,unpad_zero_count
from ..utils import zero_iv

def xor(a,b):
    # XOR two byte sequences
    return bytes(x^y for x,y in zip(a,b))

def encrypt(key,pt):
    # Encrypt using CBC: block XORed with previous ciphertext, then encrypted
    a=AESBlock(key)
    iv=zero_iv()  # Initialization Vector (all zeros for demo)
    pt=pad_zero_count(pt,16)
    c=bytearray()
    prev=iv  # First block uses IV
    for i in range(0,len(pt),16):
        blk=pt[i:i+16]
        # XOR with previous ciphertext (or IV for first block), then encrypt
        prev=a.encrypt_block(xor(blk,prev))
        c+=prev
    return bytes(c)

def decrypt(key,ct):
    # Decrypt using CBC: decrypt block, then XOR with previous ciphertext
    a=AESBlock(key)
    iv=zero_iv()
    out=bytearray()
    prev=iv  # First block uses IV
    for i in range(0,len(ct),16):
        cur=ct[i:i+16]
        # Decrypt block, then XOR with previous ciphertext
        out+=xor(a.decrypt_block(cur),prev)
        prev=cur  # Save current ciphertext for next block
    return unpad_zero_count(bytes(out),16)
