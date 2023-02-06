# Example of using different cryptographic hash functions in Python

import hashlib, binascii
import sha3

'''
SHA-3 family of functions are representatives of the "Keccak" hashes.
SHA-3 is considered highly secure.
SHA-3 cryptographic hash functions include:
    - SHA3-256
    - Keccak-256 <-- used in the Ethereum blockchain, variant of SHA3-256
    - SHA3-512
    - SHAKE-128  <-- variant of SHA3-256 with variable output message length
    - SHAKE-256  <-- variant of SHA3-512 with variable output message length
'''

# Examples of SHA-3 hashes
#SHA3-256
sha3_256hash = hashlib.sha3_256(b'hello').hexdigest()

#SHA3-512
sha3_512hash = hashlib.sha3_512(b'hello').hexdigest()

#Keccak-256
keccak256hash = sha3.keccak_256(b'hello')

#SHAKE-128
shake128hash = hashlib.shake_128(b'hello').hexdigest(256)

#SHAKE-256
shake256hash = hashlib.shake_256(b'hello').hexdigest(160)

print('========EXAMPLES OF SHA-3 HASHES=================')
print("SHA3-256('hello') =",        sha3_256hash)
print("SHA3-512('hello') =",        sha3_512hash)
#print("Keccak-256('hello') =",      binascii.hexlify(keccak256hash))
#print("\n")
print("SHAKE-128('hello', 256) =",  shake128hash)
print("SHAKE-256('hello', 160) =",  shake256hash)

'''
SHA-2 is a family of strong cryptographic hash functions and includes:
    - SHA-256 (256 bits hash)
    - SHA-384 (384 bits hash)
    - SHA-512 (512 bits hash)
'''
# Examples of SHA-2 
#SHA-256
    #sha256hash = hashlib.sha256(b'hello').digest()
sha256hash = hashlib.sha256(b'hello').hexdigest()

#SHA-384
sha384hash = hashlib.sha384(b'hello').hexdigest()
    #sha384hash = hashlib.sha384(b'hello').digest()

#SHA-512
sha512hash = hashlib.sha512(b'hello').hexdigest()
    #sha512hash = hashlib.sha512(b'hello').digest()

print('\n========EXAMPLES OF SHA-2 HASHES=================')
#print("SHA-256('hello') = ", binascii.hexlify(sha256hash))
print("SHA-256('hello') =", sha256hash)
print("SHA-384('hello') =", sha384hash)
print("SHA-512('hello') =", sha512hash)
#print("SHA-384('hello') = ", binascii.hexlify(sha384hash))
#print("SHA-512('hello') = ", binascii.hexlify(sha512hash))

'''
BLAKE2
'''
#BLAKE2s
blake2shash = hashlib.blake2s(b'hello').hexdigest()

#BLAKE2b
blake2bhash = hashlib.blake2b(b'hello').hexdigest()

print('\n========EXAMPLES OF BLAKE2 HASHES=================')
print("BLAKE2s('hello') = ", blake2shash)
print("BLAKE2b('hello') = ", blake2bhash)

'''
RIPEMD
'''
#RIPEMD-160
ripemd160 = hashlib.new('ripemd160')    # this method allows access to other algorithms that your OpenSSL library offers
ripemd160.update(b'hello')
ripemd160hash = ripemd160.hexdigest()


print('\n========EXAMPLES OF RIPEMD HASHES=================')
print("RIPDMD-160('hello') = ", ripemd160hash)