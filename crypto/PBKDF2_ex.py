import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
password = "p@$Sw0rD~1".encode("utf8")
key = pbkdf2_hmac("sha256", password, salt, 50000, 32)
print("Derived Key:", binascii.hexlify(key))