# OFB (Output Feedback) mode - generates keystream, XORs with data
from ..aes_block import AESBlock
from ..utils import zero_iv

def encrypt(key,pt):
    # Encrypt using OFB: encrypt state to get keystream, XOR with plaintext
    a=AESBlock(key)
    iv=zero_iv()
    out=bytearray()
    state=iv  # Start with IV
    for i in range(0,len(pt),16):
        state=a.encrypt_block(state)  # Encrypt state to generate keystream
        blk=pt[i:i+16]
        # XOR plaintext with keystream
        out+=bytes(x^y for x,y in zip(blk,state[:len(blk)]))
    return bytes(out)

def decrypt(key,ct):
    # OFB decryption is same as encryption (symmetric operation)
    return encrypt(key,ct)
