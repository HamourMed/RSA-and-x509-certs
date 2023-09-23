from utils import *

def emsa_pkcs1v15_pad(m: bytes, k: int) -> bytes: 
    '''pkcs#1 v1.5 padding'''
    mlen = len(m)
    rlen = k-mlen-3

    if (rlen < 8) :
        raise ValueError('Message too long')   
        
    return b"\x00\x01" + bytes([255 for i in range(rlen)]) + b"\x00" + m


def emsa_pkcs1v15_unpad(m: bytes) -> bytes:
    '''pkcs#1 v1.5 unpadding'''
    if m[0:2] != b"\x00\x01":
        raise ValueError("Invalid PKCS#1 v1.5 padding")    
    
    i = m.find(b"\x00", 2)
    if i < 0:
        raise ValueError("Invalid PKCS#1 v1.5 padding")    
    
    return m[i+1:]
