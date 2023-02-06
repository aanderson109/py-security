import scrypt

salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
password = b'p@$Sw0rD~7'
key = scrypt.hash(password, salt, 2048, 8, 1, 32)
print("derived key:", key.hex())