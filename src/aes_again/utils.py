# Utility functions for file I/O, hex conversion, and counter operations
import binascii,sys,os

def read_file(p):
    # Read file as binary data
    with open(p,'rb') as f:
        return f.read()

def write_file(p,b):
    # Write binary data to file
    with open(p,'wb') as f:
        f.write(b)

def hex_to_bytes(h):
    # Convert hex string to bytes
    return binascii.unhexlify(h.strip())

def bytes_to_hex(b):
    # Convert bytes to hex string
    return binascii.hexlify(b).decode()

def zero_iv():
    # Return 16 zero bytes (default IV - not secure for production!)
    return b'\x00'*16

def parse_key(key_hex):
    # Parse hex key and validate length (must be 16, 24, or 32 bytes)
    k=hex_to_bytes(key_hex)
    if len(k) not in (16,24,32):
        raise ValueError('key length invalid')
    return k

def parse_ctr(ctr_hex):
    # Parse hex counter and validate length (must be 16 bytes)
    c=hex_to_bytes(ctr_hex)
    if len(c)!=16:
        raise ValueError('ctr must be 16 bytes')
    return bytearray(c)  # Return as bytearray for in-place modification

def inc_ctr(c):
    # Increment counter (16-byte big-endian integer)
    # Increments from right to left, handles overflow
    for i in range(15,-1,-1):
        c[i]=(c[i]+1)&0xff  # Add 1, wrap at 256
        if c[i]!=0:break    # Stop if no carry
    return c
