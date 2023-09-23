from utils import *

def oaep_encode(m: bytes, k: int, label: bytes = b'',
                f_hash: Callable = sha1, f_mgf: Callable = mgf1) -> bytes:
    '''EME-OAEP encoding'''
    mlen = len(m)
    lhash = f_hash(label)
    hlen = len(lhash)
    ps = b'\x00' * (k - mlen - 2 * hlen - 2)
    db = lhash + ps + b'\x01' + m
    seed = os.urandom(hlen)
    db_mask = f_mgf(seed, k - hlen - 1, f_hash)
    masked_db = xor(db, db_mask)
    seed_mask = f_mgf(masked_db, hlen, f_hash)
    masked_seed = xor(seed, seed_mask)
    return b'\x00' + masked_seed + masked_db


def oaep_decode(c: bytes, k: int, label: bytes = b'',
                f_hash: Callable = sha1, f_mgf: Callable = mgf1) -> bytes:
    '''EME-OAEP decoding'''
    clen = len(c)
    lhash = f_hash(label)
    hlen = len(lhash)
    _, masked_seed, masked_db = c[:1], c[1:1 + hlen], c[1 + hlen:]
    seed_mask = f_mgf(masked_db, hlen, f_hash)
    seed = xor(masked_seed, seed_mask)
    db_mask = f_mgf(seed, k - hlen - 1, f_hash)
    db = xor(masked_db, db_mask)
    _lhash = db[:hlen]
    assert lhash == _lhash
    i = hlen
    while i < len(db):
        if db[i] == 0:
            i += 1
            continue
        elif db[i] == 1:
            i += 1
            break
        else:
            raise Exception()
    m = db[i:]
    return m 