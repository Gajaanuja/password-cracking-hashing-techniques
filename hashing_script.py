import hashlib
import bcrypt

def md5_hash (password):
	return hashlib.md5(password.encode()).hexdigest()

def sha256_hash(password):
	return hashlib.sha256(password.encode()).hexdigest()

def bcrypt_hash(password):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password.encode(), salt)


password = "mysecretpassword"
print("MD5:", md5_hash(password))
print("SHA 256:", sha256_hash(password))
print("Bcrypt:", bcrypt_hash(password))




