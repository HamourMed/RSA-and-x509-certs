from eme_oaep import *
from eme_pkcs1_v1_5 import *
from emsa_pkcs1_v1_5 import *
from emsa_pss import *


############### Keygen Primitives

def keygen(p: int = None, q: int = None, e: int = 0x010001, b: int = 2048 ) -> Tuple[Key, Key_crt]: 
    '''Create public key (exponenet e, modulus n) and private key
    (exponent d, modulus n)'''
    if p == None : 
        p = generate_prime(b // 2)

    if q == None : 
        q = generate_prime(b // 2)

    while (p * q ).bit_length() != b :
        if p > q :        
            q = generate_prime(b // 2)
        else :
            p = generate_prime(b // 2)
    
    assert is_prime(p) and is_prime(q)
    assert euclid(p, q) == 1
    assert p != q
    n = p * q   
    phi = (p - 1) * (q - 1)
    
    assert euclid(phi, e) == 1
    
    d = modinv(e, phi)

    dP = d % (p-1)
    dQ = d % (q-1)
    qInv = modinv(q, p)

    return ((n, e), (n, d, p, q, dP, dQ, qInv))



############### Encrypt Primitives

def encrypt(m: int, public_key: Key) -> int:               
    '''Encrypt an integer using RSA public key'''
    n, e = public_key
    return pow(m, e, n)


def encrypt_raw(m: bytes, public_key: Key) -> bytes:
    '''Encrypt a byte array without padding'''
    k = get_key_len(public_key)
    c = encrypt(os2ip(m), public_key)
    return i2osp(c, k)


def encrypt_oaep(m: bytes, public_key: Key, f_hash : Callable = sha1) -> bytes:
    '''Encrypt a byte array with eme oaep'''
    hlen = len(f_hash(b''))  
    k = get_key_len(public_key)
    assert len(m) <= k - hlen - 2
    return encrypt_raw(oaep_encode(m, k, f_hash=f_hash), public_key)


def encrypt_v1_5(m: bytes, public_key: Key) -> bytes:
    '''Encrypt a byte array with eme pkcs1 v1.5'''
    k = get_key_len(public_key)
    return encrypt_raw(pkcs1v15_pad(m, k), public_key)


############### Decrypt Primitives



def decrypt(c: int, private_key: Key) -> int:
    '''Decrypt an integer using RSA private key'''
    n, d = private_key
    return pow(c, d, n)


def decrypt_crt(c: int, private_key: Key_crt) -> int:
    '''Decrypt an integer using RSA private key using CRT'''
    n, d, p, q, dP, dQ, qInv = private_key
    c1 = pow(c, dP, p)
    c2 = pow(c, dQ, q)
    h = ((c1 - c2) * qInv) % p
    m = (c2 + q * h ) % n
    return m


def decrypt_raw(c: bytes, private_key: tuple) -> bytes:
    '''Decrypt a cipher byte array without padding'''
    k = get_key_len(private_key)
    if len(private_key) == 2 :        
        m = decrypt(os2ip(c), private_key)
    elif len(private_key) == 7 :
        m = decrypt_crt(os2ip(c), private_key)
    else : 
        raise ValueError('Error Key')
    return i2osp(m, k)


def decrypt_oaep(c: bytes, private_key: tuple, f_hash : Callable = sha1) -> bytes:
    '''Decrypt a cipher byte array with eme oaep'''
    k = get_key_len(private_key)
    hlen = len(f_hash(b''))  
    assert len(c) == k
    assert k >= 2 * hlen + 2
    return oaep_decode(decrypt_raw(c, private_key), k)


def decrypt_v1_5(c: bytes, private_key: tuple) -> bytes:
    '''Decrypt a cipher byte array with eme pkcs1 v1.5'''
    k = get_key_len(private_key)
    assert len(c) == k
    return pkcs1v15_unpad(decrypt_raw(c, private_key))




############### Sign Primitives

def sign_v1_5(m: bytes, private_key: Key, f_hash: Callable = sha1) -> bytes:
    '''Sign a message byte array with emsa pkcs1 v1.5'''

    k = get_key_len(private_key)
    hash = f_hash(m)   
    
    DigestInfo_encoding = {
        'md2' : b'\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x02\x05\x00\x04\x10',
        'md5' : b'\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
        'sha1' : b'\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14',
        'sha256' : b'\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
        'sha512' : b'\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40'
    }
    #Encode the HASH in a sequence("Digest Info") of ASN.1
    
    DigestInfo = DigestInfo_encoding[f_hash.__name__] +  hash
    return decrypt_raw(emsa_pkcs1v15_pad(DigestInfo, k), private_key)


def sign_pss(m: bytes, private_key: Key, f_hash: Callable = sha256) -> bytes:
    '''Sign a message byte array with emsa pss '''   
    k = get_key_len(private_key)

    return decrypt_raw(emsa_pss_encode(m, k,f_hash=f_hash), private_key= private_key)



############### Verify Primitives 


def verify_v1_5(c: bytes, m: bytes, public_key: Key , f_hash: Callable = sha1) -> bool :
    '''verfiy a cipher and a massage byte array with emsa pkcs1 v1.5'''
    k = get_key_len(public_key)
    hash = f_hash(m)
    H = emsa_pkcs1v15_unpad(encrypt_raw(c, public_key))
    DigestInfo_encoding = {
        'md2' : b'\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x02\x05\x00\x04\x10',
        'md5' : b'\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
        'sha1' : b'\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14',
        'sha256' : b'\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
        'sha512' : b'\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40'
    }
    
    DigestInfo = DigestInfo_encoding[f_hash.__name__] +  hash
    
    if DigestInfo != H : 
        return False
    
    return True


def verify_pss(c: bytes, m: bytes, public_key: Key, f_hash: Callable = sha256) -> bool:
    '''verfiy a cipher and a massage byte array with emsa pss'''

    k = get_key_len(public_key)
    dc = encrypt_raw(c, public_key=public_key)
    return emsa_pss_verify(dc, m, k, f_hash=f_hash)
