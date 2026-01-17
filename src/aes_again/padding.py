# Padding functions for AES block cipher operations
# AES requires data to be multiple of 16 bytes

def pad_zero_count(b,block_size=16):
    # Pad data to multiple of block_size using zero-count padding
    # Format: data + zeros + padding_length
    r=len(b)%block_size
    p=block_size if r==0 else block_size-r  # Calculate padding needed
    if p<1 or p>block_size:raise ValueError('pad')
    return b+b'\x00'*(p-1)+bytes([p])  # Add zeros and padding length byte

def unpad_zero_count(b,block_size=16):
    # Remove padding from data
    # Reads padding length from last byte and removes that many bytes
    if len(b)==0 or len(b)%block_size!=0:raise ValueError('bad length')
    p=b[-1]  # Get padding length from last byte
    if p<1 or p>block_size:raise ValueError('bad pad')
    if b[-p:-1]!=b'\x00'*(p-1):raise ValueError('bad pad')  # Verify zeros
    return b[:-p]  # Return data without padding
