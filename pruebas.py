import bcrypt

texto = input('-:        ')
pwd = texto.encode('utf-8')
salt = b'$2b$12$ASCDyiUrL20F696Dwg8Iw.'
encriptado = bcrypt.hashpw(pwd, salt)

encriptedContra = str(encriptado)
encriptedContra = encriptedContra[2:-1]
print(encriptado)
print(encriptedContra)