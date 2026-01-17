# CFB (Cipher Feedback) mode - turns block cipher into stream cipher
from ..aes_block import AESBlock
from ..utils import zero_iv

def encrypt(key,pt):
    # Encrypt using CFB: encrypt state to get keystream, XOR with plaintext
    a=AESBlock(key)
    iv=zero_iv()
    out=bytearray()
    state=iv  # Start with IV
    for i in range(0,len(pt),16):
        ks=a.encrypt_block(state)  # Encrypt state to get keystream
        blk=pt[i:i+16]
        ct=bytes(x^y for x,y in zip(blk,ks[:len(blk)]))  # XOR with keystream
        out+=ct
        # Update state: use ciphertext (or partial state + ciphertext)
        if len(blk)==16:state=ct
        else:state=(state[len(blk):]+ct)
    return bytes(out)

def decrypt(key,ct):
    # Decrypt using CFB: encrypt state to get keystream, XOR with ciphertext
    a=AESBlock(key)
    iv=zero_iv()
    out=bytearray()
    state=iv
    for i in range(0,len(ct),16):
        ks=a.encrypt_block(state)  # Encrypt state to get keystream
        blk=ct[i:i+16]
        pt=bytes(x^y for x,y in zip(blk,ks[:len(blk)]))  # XOR with keystream
        out+=pt
        # Update state: use ciphertext (or partial state + ciphertext)
        if len(blk)==16:state=blk
        else:state=(state[len(blk):]+blk)
    return bytes(out)
