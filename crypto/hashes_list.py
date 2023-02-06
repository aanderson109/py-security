import hashlib, binascii
from Crypto.Hash import keccak
import whirlpool

data = b'hello'

sha224hash = hashlib.sha224(data).hexdigest()
print("SHA-224:             ", sha224hash)

sha256hash = hashlib.sha256(data).hexdigest()
print("SHA-256:             ", sha256hash)

sha3_224hash = hashlib.sha3_224(data).hexdigest()
print("SHA3-224:            ", sha3_224hash)

sha3_256hash = hashlib.sha3_256(data).hexdigest()
print("SHA3-256:            ", sha3_256hash)

sha3_384hash = hashlib.sha3_384(data).hexdigest()
print("SHA3-384:            ", sha3_384hash)

blake2shash = hashlib.new('blake2s', data).hexdigest()
print("BLAKE2s:             ", blake2shash)

ripemd160hash = hashlib.new('ripemd160', data).hexdigest()
print("RIPEMID-160:         ", ripemd160hash)

keccak256hash = keccak.new(data=b'hello', digest_bits=256).hexdigest()
print("Keccak-256:          ", keccak256hash)

keccak384hash = keccak.new(data=b'hello', digest_bits=384).hexdigest()
print("Keccak-256:          ", keccak384hash)

whirlpoolhash = whirlpool.new(data).hexdigest()
print("Whirlpool:           ", whirlpoolhash)