import hashlib


def gen_passwd(passwd):
    sha = hashlib.sha512()
    sha.update(passwd.encode())
    return sha.hexdigest()