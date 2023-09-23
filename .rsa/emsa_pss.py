from utils import *

def emsa_pss_encode(m: bytes, k: int,
                f_hash: Callable = sha256, f_mgf: Callable = mgf1) -> bytes:
    
    mHash = f_hash(m)
    hlen = len(mHash)
    salt = os.urandom(hlen)
    
    m_prime = b'\x00' * 8 + mHash + salt 
    H = f_hash(m_prime)
    pslen = k - 2 * hlen - 2

    db = os.urandom(pslen) + b'\x01' + salt
    mask = f_mgf(H, k - hlen - 1, f_hash)
    masked_db= xor(db, mask)
    

    return masked_db + H + b'\xbc'

def emsa_pss_verify(c: bytes, m: bytes, k: int,
                f_hash: Callable = sha256, f_mgf: Callable = mgf1) -> bytes:
    h = f_hash(m)
    hlen = len(h)
    if c[-1:] != b'\xbc':
        return False
    
    masked_db = c[:k-hlen-1]
    H = c[k-hlen-1 : k-1]
    mask = f_mgf(H,k-hlen-1,f_hash)
    db = xor(masked_db, mask)

    salt = db[k-2*hlen-1 : k-hlen-1]

    h_prime = f_hash(b'\x00' * 8+ h + salt)
    
    if h_prime != H:
        return False      

    return True