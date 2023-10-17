import tkinter as tk
import tkinter.font as tkFont
import subprocess
import sys
import bcrypt
salt = b'$2b$12$ASCDyiUrL20F696Dwg8Iw.'


argumentos = sys.argv
carnet = argumentos[len(argumentos) - 1]

DataProfesor = []
crss = []

with open(F'Pantallas/Datos/Profesores/{carnet}.txt') as Pbd:
    leer = Pbd.read()
    lectura = leer.split('///\n')
    DataProfesor = lectura[0].split(',')
    crss = lectura[1]

vista = tk.Tk()
vista.geometry('300x400')
vista.title(F'Cambiar contraseña {carnet}')

firstLbl = tk.Label(vista, text = 'Contraseña Actual')
firstLbl.pack(pady = 10)

actual = tk.Entry(vista)
actual.pack(pady = 10)

SecLbl = tk.Label(vista, text = 'Nueva Contraseña')
SecLbl.pack(pady = 10)

Nueva = tk.Entry(vista)
Nueva.pack(pady = 10)

TrdLbl = tk.Label(vista, text = 'Confirmar Contraseña')
TrdLbl.pack(pady = 10)

confirmar = tk.Entry(vista)
confirmar.pack(pady = 10)


def reescribirData():

    alumnoNew = []
    alumnoD = ','.join(DataProfesor)
    alumnoNew.append(alumnoD)
    alumnoNew.append('///\n')
    alumnoNew.append(crss)

    alumnoNew = ''.join(alumnoNew)
    print(alumnoNew)

    with open(F'Pantallas/Datos/Profesores/{carnet}.txt', 'w') as data:
        print('Hola')
        data.write(alumnoNew)



def verificacion():
    act = actual.get()
    new = Nueva.get()
    conf = confirmar.get()

    criptContra = bytes(DataProfesor[6],'utf-8')
    cripAct = bytes(act,'utf-8')

    if  bcrypt.checkpw(cripAct,criptContra):
        for char in new:
            char = ord(char)
            if char >= 32 and char <= 47:
                validSimb = 1
            if char > 47 and char <= 57:
                validNum = 1
            if char >= 65 and char <= 90:
                validMay = 1
            if char >= 97 and char <= 122:
                validMin = 1
            print(char)
        if validSimb == 1 and validNum == 1 and validMay == 1 and validMin == 1 and len(new) >= 8:
            if new == conf:
                new = bytes(new, 'utf-8')
                NewEncriptedContra = bcrypt.hashpw(new, salt)
                encriptedContra = str(NewEncriptedContra)
                encriptedContra = encriptedContra[2:-1]
                DataProfesor[6] = encriptedContra

                reescribirData()
            else:
                print('confirme su sontraseña correctamente')
                subprocess.run(['python', 'Pantallas/error.py', 'Datos Incorrectos', 'Confirme su contraseña correctamente'])
        else:
            print('contraseña totalmente INVALIDA')
            subprocess.run(['python', 'Pantallas/error.py', 'Datos Incorrectos', 'Su contraseña debe tener: Mayusculas, Minusculas\n Minimo un numero y un simbolo [  !, ", #, $, %, &, /,), (, *, +, -, ·	]'])

    else: 
        print('coloque su antigua contraseña correctamente')
        subprocess.run(['python', 'Pantallas/error.py', 'Datos Incorrectos', 'Coloque su antigua contraseña'])


btn = tk.Button(vista, text ='Guardar', command = verificacion)
btn.pack()

vista.mainloop()