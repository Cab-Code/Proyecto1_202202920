import bcrypt

intro = input('-Datos: ')

salt = b'$2b$12$ASCDyiUrL20F696Dwg8Iw.'

encod = bytes(intro, 'utf-8')

E = bcrypt.hashpw(encod, salt)

print(E)