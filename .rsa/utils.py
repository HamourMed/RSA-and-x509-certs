from math import sqrt, ceil
import os
import copy
import hashlib
import random
from typing import Tuple, Callable
import pyasn1.codec.der.decoder
import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64


Key = Tuple[int, int] # (n, e), (n, d)
Key_crt = Tuple[int, int, int, int, int, int, int]    # n, d, p, q, dP, dQ, qInv

def euclid(a: int, b: int) -> int:
    '''Calculate the GCD of a and b using Euclid's algorithm'''
    while b != 0:
        a, b = b, a % b
    return a


def extend_euclid(a: int, b: int) -> int:
    '''Returns a tuple (r, s, t) such that r = gcd(a, b) and r = sa + tb.'''
    
    s, s_prev = 0, 1
    t, t_prev = 1, 0
    r, r_prev = b, a
    
    while r != 0:
        quotient = r_prev // r
        r_prev, r = r, r_prev - quotient * r
        s_prev, s = s, s_prev - quotient * s
        t_prev, t = t, t_prev - quotient * t
    
    gcd = r_prev
    return s_prev, t_prev, gcd


def modinv(a: int, b: int) -> int:
    '''Calculate the Modular Inverse'''
    # return modular inv of a in (Z/bZ)*
    x, y, q = extend_euclid(a, b)
    if q != 1:
        return None
    else:
        return x % b


def is_prime_trial_division(n: int) -> bool:
    '''Test if a given integer n is a prime number using trial division'''
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


# prime numbers with 1000
known_primes = [2] + \
    [x for x in range(3, 1000, 2) if is_prime_trial_division(x)]


def miller_rabin_primality_test(p, s=5):
    '''Test if a given integer n is a prime number using miller rabin test'''
    if p == 2: # 2 is the only prime that is even
        return True
    if not (p & 1): # n is a even number and can't be prime
        return False

    p1 = p - 1
    u = 0
    r = p1  # p-1 = 2**u * r

    while r % 2 == 0:
        r >>= 1
        u += 1

    # at this stage p-1 = 2**u * r  holds
    assert p-1 == 2**u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = pow(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = pow(a, 2**i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p-2)
        if witness(a):
            return False

    return True


def is_prime(n: int, precision: int = 7) -> bool:
    '''Test if a given integer is a prime number'''
    assert n > 1
    if n in known_primes:
        return True
    elif n < 100000:
        return is_prime_trial_division(n)
    else:
        return miller_rabin_primality_test(n, precision)
    
def generate_prime(n: int) -> int:
    '''Generate a prime number'''
    assert n > 0 and n < 4096

    x = random.getrandbits(n) | ((2**(n-1))+(2**(n-3)) + 1)

    while not miller_rabin_primality_test(x, s=7):
        x = random.getrandbits(n) | ((2**(n-1))+(2**(n-3)) + 1)
    
    return x
    

def get_key_len(key: tuple) -> int:
    '''Get the number of octets of the public/private key modulus'''
    n = key[0]
    return n.bit_length() // 8


def os2ip(x: bytes) -> int:
    '''Converts an octet string to a nonnegative integer'''
    return int.from_bytes(x, byteorder='big')


def i2osp(x: int, xlen: int) -> bytes:
    '''Converts a nonnegative integer to an octet string of a specified length'''
    return x.to_bytes(xlen, byteorder='big')


def sha1(m: bytes) -> bytes:
    '''SHA-1 hash function'''
    hasher = hashlib.sha1()
    hasher.update(m)
    return hasher.digest()

def sha256(m: bytes) -> bytes:
    '''SHA-256 hash function'''
    hasher = hashlib.sha256()
    hasher.update(m)
    return hasher.digest()

def mgf1(seed: bytes, mlen: int, f_hash: Callable = sha1) -> bytes:
    '''MGF1 mask generation function with SHA-1'''
    t = b''
    hlen = len(f_hash(b''))
    for c in range(0, ceil(mlen / hlen)):
        _c = i2osp(c, 4)
        t += f_hash(seed + _c)
    return t[:mlen]


def xor(data: bytes, mask: bytes) -> bytes:
    '''Byte-by-byte XOR of two byte arrays'''
    masked = b''
    ldata = len(data)
    lmask = len(mask)
    for i in range(max(ldata, lmask)):
        if i < ldata and i < lmask:
            masked += (data[i] ^ mask[i]).to_bytes(1, byteorder='big')
        elif i < ldata:
            masked += data[i].to_bytes(1, byteorder='big')
        else:
            break
    return masked


def private_key_pem(n: int, e: int, d: int, p: int, q: int, dP: int, dQ: int, qInv: int) -> str:
    '''Create a private key PEM file'''
    template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for x in [0, n, e, d, p, q, dP, dQ, qInv]:
        seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodebytes(der).decode('ascii')) #


def public_key_pem(n: int, e: int) -> str:
    '''Create a public key PEM file'''
    template = '-----BEGIN RSA PUBLIC KEY-----\n{}-----END RSA PUBLIC KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for x in [n, e]:
        seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodebytes(der).decode('ascii')) #