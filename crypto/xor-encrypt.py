# XOR Encryption Algorithim

def binary(num, length=8):
    b = bin(num).lstrip("0b")
    b = "0" *(length-len(b)) + b
    return b

def hexa(num, length=2):
    h = hex(num).lstrip("0x").upper()
    h = "0" *(length-len(h)) + h
    return h

plaintext = input("Please enter a message to encryt:\n")
key = "the_key"
key_length = len(key)
cipher_ascii = ""
cipher_den = ""
cipher_hex = ""
cipher_bin = ""

for i in range(0, len(plaintext)):
    j = i % key_length

    xor = ord(plaintext[i]) ^ ord(key[j])
    cipher_ascii = cipher_ascii + chr(xor)
    cipher_den = cipher_den + str(xor) + " "
    cipher_hex = cipher_hex + hexa(xor) + " "
    cipher_bin = cipher_bin + binary(xor) + " "

print("\nCipher (Ascii): " + cipher_ascii)
print("\nCipher (Denary): " + cipher_den)
print("\nCipher (Hexadecimal): " + cipher_hex)
print("\nCipher (Binary): " + cipher_bin)