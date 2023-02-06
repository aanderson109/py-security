import hashlib, hmac

MAC = hmac.new(b'key', b'message', hashlib.sha256).hexdigest()
print(MAC)