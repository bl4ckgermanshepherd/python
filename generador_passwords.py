#Today I learn how to make random passwords, how to encrypt and how to check if a string match with a hash
#The encryption will wive you the password and the hash at the same time like this "{>kXds%=+*72<Ky}.t;¿ --> pbkdf2:sha256:260000$35XRJ86F0rDeIt87$fa897cc65120f956dd4a2db441a469fbd5a10666fce610ce366e5813d0f54c1a".

import random

import werkzeug

from werkzeug.security import generate_password_hash, check_password_hash

minus = "abcdefghijklmnp`qrstuvwxyz"
mayus = minus.upper()
numbers = "0123456789"
symbols = "@()[]{}*,;/-_¿?.!¡%<#>&+%="
base = minus+mayus+numbers+symbols
large = 20


muestra = random.sample(base,large)
password ="".join(muestra)
password_encrypted = generate_password_hash(password)
print("{} --> {}".format(password, password_encrypted))

print(check_password_hash(password_encrypted, password))
