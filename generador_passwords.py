import random

import werkzeug

from werkzeug.security import generate_password_hash, check_password_hash

minus = "abcdefghijklmnp`qrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?.!¡%<#>&+%="
base = minus+mayus+numeros+simbolos
longitud = 20


muestra = random.sample(base,longitud)
password ="".join(muestra)
password_encriptado = generate_password_hash(password)
print("{} --> {}".format(password, password_encriptado))

print(check_password_hash(password_encriptado, password))