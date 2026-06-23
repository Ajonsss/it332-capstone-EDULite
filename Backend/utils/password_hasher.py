import bcrypt

def hash_password(password):
    # returns bytes → we convert to string for SQLite storage
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # store as TEXT in DB


def verify_password(password, hashed_password):
    # convert DB string back to bytes
    hashed_password = hashed_password.encode('utf-8')

    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password
    )