# CTR (Counter) mode - uses counter to generate keystream, XORs with data
from ..aes_block import AESBlock
from ..utils import parse_ctr,inc_ctr

def encrypt(key,pt,counter_hex=None):
    # Encrypt using CTR: encrypt counter to get keystream, XOR with plaintext
    if counter_hex is None:raise ValueError('ctr required')
    ctr=parse_ctr(counter_hex)
    a=AESBlock(key)
    out=bytearray()
    for i in range(0,len(pt),16):
        # Encrypt counter to generate keystream
        ks=a.encrypt_block(bytes(ctr))
        blk=pt[i:i+16]
        # XOR plaintext with keystream
        out+=bytes(x^y for x,y in zip(blk,ks[:len(blk)]))
        inc_ctr(ctr)  # Increment counter for next block
    return bytes(out)

def decrypt(key,ct,counter_hex=None):
    # CTR decryption is same as encryption (symmetric operation)
    return encrypt(key,ct,counter_hex)
