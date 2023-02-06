


# Hash Functions
## Secure Hash Algorithms
### SHA-3
* backfill SHA-3 section

### SHA-2
* backfill SHA-2 section

### BLAKE2
BLAKE2, and its variants, is a family of fast, highly secure cryptographic hash functions. They are capable of calculating 160-bit, 224-bit, 256-bit, 384-bit, and 512-bit digests.

BLAKE2s is optimized for 32-bit microprocessors while BLAKE2b is tailored for 64-bit microprocessors.

BLAKE2's strength is comparable to SHA-3 even though it is used with less frequency.

### RIPEMD-160
RIPEMD-160 is a 160-bit version of RIPEMD. As a secure hash function, the 160-bit flavor is used with widely with developers in things like PGP and Bitcoin.

The 128, 256, and 320-bit varieties of RIPDMD are not particularly popular and their strength is disputed.

## Insecure Hash Functions
Some older algorithms are considered insecure because of collisions or other weaknesses. They are not safe to use. These algorithms include:
* MD2
* MD4
* MD5
* SHA-0
* SHA-1
* Panama
* HAVAL
* Tiger

## Other Hash Functions
There are some popular alternatives to SHA-2, SHA-3, and BLAKE2 that are believed to have relatively strong security. These algorithms include:
* **Whirlpool** --> a secure hash function, produces 512-bit digests.
* **SM3** --> standardized by the Chinese government; similar to SHA-256 and produces 256-bit digests.
* **GOST** --> specifically GOST R 34.11-94 and described in RFC 4357; is the Russian national standard, and produces 256-bit digests.

## Cryptographic Hash Functions & Python
Python's `hashlib` library is particularly useful for using a variety of the most popular hash functions. Some important notes about this:
* Data is input as a **bytes object** so the output will be a bytes object as well.
    - the input string will need to be encoded

It's possible to either use the method `.digest()` or `.hexdigest()`.
* `.digest()` returns the digest as a bytes object of size `digest_size`
* `.hexdigest()` returns the digest as a string object of double length with only hexadecimal digits.

While `hashlib` will work for many hash functions, some algorithms like `Keccak-256` require additional libraries.

For `Keccak-256`, install the library *pycryptodoome*
`pip install pycryptodome`

For `Whirlpool`, install the library *whirlpool*
`pip install whirlpool`

## Proof-of-Work
Proof-of-Work (PoW) algorithms, like those used on the blockchain, are unique hash functions designed to be computationally-intensive and memory-intensive. "ASIC-resistant" functions are meant to be difficult for hardware devices.

The following algorithms are intended to be used as PoW algorithms since they are slow to calculate and typically require GPU hardware or powerful CPU resources:
* ETHash
* Equihash
* CryptoNight
* Cookoo Cycle

### ETHash
ETHash is used in the Ethereum blockchain. It is a proof-of-work hash function and believed to be ASIC-resistant.

This is how the algorithm works:
* A **seed** is computed for each block (based on the entire chain up to the current block)
* From that seed, a 16 Megabyte (MB) pseudo-random cache is calculated
* From that cache, a 1 Gigabyte (GB) dataset is extracted for mining
* Mining involves hashing together the random slices of the dataset

### Equihash
Equihash is a proof-of-work hash function used in Zcash and Bitcoin Gold. It is believed to be ASIC-resistant.

Equihash works like so:
* BLAKE2b is used to calculate a 50 MB hash dataset from previous blocks in the chain.
* The *Generalized Birthday Problem* is soolved over the hashed data.
* The solution is put through the SHA-256 function twice to produce the final digest.

# MAC & Key Derivation
Message Authentication Codes (MACs), Hash-Based Message Authentication Code (HMAC), and Key Derivation Functions (KDFs) are critical tools in cryptography.

## Message Authentication Code (MAC)
A MAC is calculated with a specific key and message:
`auth_code = MAC(key, message)`
MACs behave like hashes: a minor change in the message or key results in a unique MAC value and they are supposed to be irreversible (i.e., you cannot derive the message from the MAC). MACs are sometimes called *keyed hash functions*.

### MAC Algorithms
A variety of algorithms are used for calculating MACs. The most popular are based on standard hashing algorithms.
* Hash-based MAC (HMAC-SHA256)
* Keccak-based MAC (KMAC)

Some MAC algorithms are bsaed on symmetric ciphers:
* Cipher-based MAC (CMAC)
* Galois MAC (GMAC)
* Poly1305

Other algorithms include:
* MAC based on Universal Hashing (UMAC)
* High-Performance Block Cipher-Based MAC (VMAC)
* Simple, Fast, Secure MAC (SipHash)

### When Are MACs Used?
Example:
* Two people exchange a certain secret MAC key (i.e., pre-shared key)
* We receive a message + authentication code from somewhere (internet, blockchain, email, etc.)
* We want to ensure the message is not tampered (i.e., both the key and message are correct)
    - We calculate the MAC and compare it to our pre-shared, secret MAC
    - the MAC will be incorrect if tampering as occurred

### MACs for Authenticated Encryption
Authenticated Encryption is when we want to be sure the decryption password is correct and the message is the same as the original (before encryption).

* Derive a key from the password.
    - Used as the key for the MAC algorithm
* Encrypt the message using the derived key and store the ciphertext in the output
* Calculate the MAC code using the derived key and original message
    - Append result to the output
When we decrypt the encrypted message (ciphertext + MAC):
* Derive a key from the password
* Decrypt the message using the derived key
* Calculate a MAC code using the derived key + the decrypted message
    - IF the calculated MAC code **matches** the MAC code in the encrypted message --> password is correct
    - IF the calculated MAC code **does not match** the MAC code --> password is incorrect

Some authenticated encryption algorithms (AES-GCM, ChaCha20-Poly1305) integrate the MAC calculation into the encryption algorithm and the MAC verification into the decryption algorithm.

MAC is stored along with the ciphertext and does not reveal the password or message.

### MAC-Based Pseudo-Random Generator
MAcs are also used for pseudo-random generator functions. Start from certain *salt* (constant number or the current date and time or some other random value) and some *seed* number (last random number generated). Calculate the *next_seed* as follows:
`next_seed = MAC(salt, seed)`

## HMAC & Key Derivation
Calculating `hash_function(key + message)` to generate a MAC is considered insecure. Rather, an HMAC algorithm should be used.

An HMAC is a MAC calculated using a cryptographic hash function.
`HMAC(key, message, hash_function) --> hash`
The output is a MAC code comprised of a digest mixed with a secret key. It has the cryptographic attributes associated with hashing: irreversibility, collision resistant, etc.

The hash function can be any function like SHA-256, SHA-512, RIPEMD-160, SHA3-256, or BLAKE2s.

HMACs are used for message authenticity, message integrity, and sometimes key derivation.

### Key Derivation Functions (KDFs)
A KDF is a function which transforms a variable-length password to fixed-length key (sequence of bits):
`function(password) --> key`
A simple KDF function would be to use SHA256 and hash the password. However, that is insecure as simple hashes are vulnerable to dictionary attacks.

A more complicated KDF would be to derive a password by calculating `HMAC(salt, message, SHA256)` using a random value called **salt** which is stored along with the derived key and used later to derive the same key again from the password.

HMAC-Based Key Derivation (HKDF) is less secure than modern KDFs, so it's recommended to use stronger key derivation functions like:
* PBKDF2
* Bcrypt
* Scrypt
* Argon2

## PBKDF2
PBKDF2 is a simple cryptographic key derivation function that is resistant to dictionary attacks and rainbow table attacks. Based on iteratively deriving HMAC many times with some padding. PBKDF2 algorithm is described in RFC 2398.

PBKDF2 takes several input parameters and produces a derived key as output:
`key = pbkdf2(passwoord, salt, iterations-count, hash-function, derived-key-len)`

Input data consists of:
* **password** --> array of bytes/string
* **salt** --> securely-generated random bytes
* **iterations-count** --> any number
* **hash-function** --> for calculating the HMAC
* **derived-key-len** --> for the output
Output data is the derived key of requested length.

PBKDF allows you to configure the number of iterations and thus configure the time required to derive the key.
* Slower derivation --> high login time, slower decryption, etc. and higher resistance to password cracking attacks
* Faster derivation --> short  login time, faster decryption, lower resistance to password cracking attacks
* PBKDF2 is not resistant to GPU attacks and ASIC attacks.

## Modern Key Derivation Functions
PBKDF2 has major weaknesses, Scrypt and Argon2 are designed to be resistant to dictionary attacks, GPU attacks, ASIC attacks.

### Scrypt
RFC 7914. Strong KDF; memory intensive, designed to prevent GPU, ASIC, FPGA attacks.

Scrypt algorithm takes several input parameters and produces the key as output:
`key = Scrypt(password, salt, N, r, p, derived-key-len)`
Parameters are:
* `N` --> iterations count
* `r` --> block size
* `p` --> parallelism factor (usually 1)
* `password` --> input password
* `salt` --> securely-generated random bytes
* `derived-key-length` --> how many bytes to generate as output
Memory in Scrypt is accessed in strongly dependent order at each step, so the memory access speed is the algorithms bottleneck.
`memory required = 128 * N * r * p bytes`
Choosing parameters depends on how much you want to wait, the level of security you want to achieve:
* Interactive Login Sample: N=16384, r=8, p=1 (RAM = 2 MB)
* File Encryption Sample: N=1048576, r=8, p=1 (RAM = 1 GB)



# Sources
BLAKE   (https://en.wikipedia.org/wiki/BLAKE_(hash_function))
BLAKE2  (https://en.wikipedia.org/wiki/BLAKE_(hash_function)#BLAKE2)
RIPDMD  (https://en.wikipedia.org/wiki/RIPEMD)
Whirlpool Library
* https://pypi.org/project/Whirlpool/#:~:text=python%2Dwhirlpool&text=It%20is%20a%20secure%20and,from%20a%20variable%2Dlength%20message.
* https://github.com/oohlaf/python-whirlpool

Generalized Birthday Problem
* https://www.iacr.org/archive/crypto2002/24420288/24420288.pdf
* https://blog.sigmaprime.io/zcash-theoretically-improving-mining-speeds.html#:~:text=Equihash%20is%20an%20algorithm%20based,people%20have%20the%20same%20birthday.
* https://en.wikipedia.org/wiki/Birthday_problem

Programmatic Proof-of-Work
* https://github.com/ifdefelse/ProgPOW

Equihash
* https://github.com/tromp/equihash
* https://www.cryptolux.org/images/b/b9/Equihash.pdf

ETHash
* https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/mining-algorithms/
* https://github.com/lukovkin/ethash

Scrypt
* https://en.wikipedia.org/wiki/Scrypt

Bcrypt
* https://en.wikipedia.org/wiki/Bcrypt

Argon2
* https://en.wikipedia.org/wiki/Argon2
