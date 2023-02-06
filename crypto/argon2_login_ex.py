import argon2

ph = argon2.PasswordHasher()

def login(db, user, password):
    hash = db.get_password_hash_for_user(user)

    #verify password
    ph.verify(hash, password)

    #now that we have the cleartext password,
    # check the hash's parameters and if outdated,
    # rehash the user's password in the database
    if ph.check_needs_rehash(hash):
        db.set_password_hash_for_user(user, ph.hash(password))