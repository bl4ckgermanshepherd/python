#Today I learn how to make random passwords, how to encrypt and how to check if a string match with a hash

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
