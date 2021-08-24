import hashlib 

def hashFunc(password):
    hash = hashlib.md5(password.encode())
    return(hash.hexdigest())


