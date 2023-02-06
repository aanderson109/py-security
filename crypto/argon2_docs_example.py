import argon2

ph = argon2.PasswordHasher()                        # calls PasswordHasher() for future password hashing 
hash = ph.hash("correct horse battery staple")      # calls .hash() method from PasswordHasher() to hash the string
print("Argon2 Hash: ", hash)                        # prints digest from previous hashing

verification = ph.verify(hash, "correct horse battery staple")  # calls .verify() method to compare the hash value with the given string
print(verification)                                             # prints the boolean result of the comparison

verification = ph.verify(hash, "haha")                          # calls .verify() method to compare the hash value with the given string
print(verification)                                             # prints the boolean result of the comparison
