import argon2, binascii

hashing = argon2.PasswordHasher(time_cost=16, memory_cost=2**15, parallelism=2,
                                hash_len=32, type=argon2.low_level.Type.ID)

digest = hashing.hash(b'password')  # output is an encoded hash returned as a str

print("Argon2 Digest:   ", digest)

try:
    hashing.verify(digest, "password")
    print("\ncorrect password!")
except:
    print("Argon2 verify (incorrect password):  ", False)