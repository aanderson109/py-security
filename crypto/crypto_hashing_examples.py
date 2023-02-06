import hashlib, binascii
from Crypto.Hash import keccak

text = 'hello'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).hexdigest()
print("SHA-256:         ", sha256hash)

sha3_256hash = hashlib.sha3_256(data).hexdigest()
print("SHA3-256:        ", sha3_256hash)

blake2shash = hashlib.new('blake2s', data).hexdigest()
print("BLAKE2s:         ", blake2shash)

ripemd160hash = hashlib.new('ripemd160', data).hexdigest()
print("RIPEMID-160:     ", ripemd160hash)

keccak256hash = keccak.new(data=b'hello', digest_bits=256).hexdigest()
print("Keccak-256:      ", keccak256hash)