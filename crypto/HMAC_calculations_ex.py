import hashlib, hmac

def hmac_sha256(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

key     = b'12345'
message = b'sample message'

print(hmac_sha256(key, message))

def hmac_sha384(key, message):
    return hmac.new(key, message, hashlib.sha384).hexdigest()

key_one = b'cryptography'
key_two = b'again'

message_one = b'hello'
message_two = b'hello'

# calculate HMAC for first message + key combo
print(hmac_sha384(key_one, message_one))

# calculate the HMAC for second message + key combo
print(hmac_sha384(key_two, message_two))