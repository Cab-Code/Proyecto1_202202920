import tkinter as tk
import tkinter.font as tkFont
import subprocess
import sys
import bcrypt


print('nueva ventana')
argumentosPrograma = sys.argv

carnet = argumentosPrograma[1]
alumnoData = []
alumnoCursos = []
alumnoData = []
with open(F'Pantallas/Datos/Alumnos/{carnet}.txt') as BaseDatos:
    leer = BaseDatos.read()
    alumno = leer.split('///\n')
    alumnoData = alumno[0]
    alumnoCursos = alumno[1]
    alumnoData = alumnoData.split(',')

vista = tk.Tk()
vista.title('Configuracion De Usuario')
vista.geometry('750x600+0+0')
print(alumnoData)
carnet = alumnoData[0]
nombre = alumnoData[1]
apelli = alumnoData[2]
Dpi = alumnoData[3]
fechaN = alumnoData[4]
tel = alumnoData[5]
userName = alumnoData[6]
correo = alumnoData[7]
contra = alumnoData[8]

def reescribirData():

    alumnoNew = []
    alumnoD = ','.join(alumnoData)
    alumnoNew.append(alumnoD)
    alumnoNew.append('///\n')
    alumnoNew.append(alumnoCursos)

    alumnoNew = ''.join(alumnoNew)
    print(alumnoNew)

    with open(F'Pantallas/Datos/Alumnos/{carnet}.txt', 'w') as data:
        data.write(alumnoNew)
        print('Hola')




def cambioTel(dat):
    try:
        if len(dat) != 8:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El numero de telefono debe tener 8 digitos'])
        numeroNew = int(dat)
        alumnoData[5] = str(numeroNew)
    except:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'ingrese su numero de telefono sin espacion ni guiones solo numeros'])
    reescribirData()

def cambiarCorreo(dat):
    alumnoData[6] = dat
    reescribirData()

def validarCorreo(dat):
    valid = 0
    v = 0
    for letra in dat:
        if letra == '@':
            valid = 1
        if letra == '.' and valid == 1:
            v = 4
               
    if v == 4:
        print('Correo valido')  
        cambiarCorreo(dat)
    else:   
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'ingrese un correo electronico valido (ejemplo: userName@gmail.com)'])


def validarContraseña():
    print('hola')
        
    reescribirData()

mainCtn = tk.Frame(master = vista, background = 'red')
mainCtn.pack()

firstCtn = tk.Frame(master = mainCtn, background = 'blue')
labelCarnet = tk.Label(master = firstCtn, text = carnet)
firstCtn.grid(row = 0, column = 0, pady = 10, padx = 20)
labelCarnet.grid(row = 0, column = 0)

secondCtn = tk.Frame(master = mainCtn, background = 'blue')
labelName = tk.Label(master = secondCtn, text = nombre)
labelApellido = tk.Label(master = secondCtn, text = apelli)
labelFechaN = tk.Label(master = secondCtn, text = fechaN)
TelCotn = tk.Frame(master = secondCtn)
LabelTel = tk.Label(master = TelCotn, text = tel, )
entryTel = tk.Entry(master = TelCotn)
BtnTel = tk.Button(master = TelCotn, text = 'actualizar telefono', command = lambda: cambioTel(entryTel.get()))
CorreoCotn = tk.Frame(master = secondCtn)
LabelCorreo = tk.Label(master = CorreoCotn, text = correo)
entryCorreo = tk.Entry(master = CorreoCotn)
BtnCorreo = tk.Button(master = CorreoCotn, text = 'actualizar correo', command = lambda: validarCorreo(entryCorreo.get())) 

secondCtn.grid(row = 2, column = 0,pady = 10, padx = 20)
labelName.grid(row = 0, column = 0,pady = 15, padx = 20)
labelApellido.grid(row = 0, column = 1,pady = 15, padx = 20)
labelFechaN.grid(row = 1, column = 0,pady = 15, padx = 20)
TelCotn.grid(row = 1, column = 1,pady = 8, padx = 20)
LabelTel.grid(row = 0, column = 0,pady = 8, padx = 20)
entryTel.grid(row = 1, column = 0, pady = 8, padx = 20)
BtnTel.grid(row = 1, column = 1, pady = 8, padx = 20)
CorreoCotn.grid(row = 2, column = 0, pady = 8, padx = 20)
LabelCorreo.grid(row = 0, column = 0, pady = 8, padx = 20)
entryCorreo.grid(row = 1, column = 0, pady = 8, padx = 20)
BtnCorreo.grid(row = 1, column = 1, pady = 8, padx = 20)

contraseñaCtn = tk.Frame(master = mainCtn, background = 'green')
contraseñaCtn.grid(row = 3, column = 0)
labelInstrucciones = tk.Label(master = contraseñaCtn, text = 'Cambiar Contraseña')
labelInstrucciones.pack()
labelA = tk.Label(master = contraseñaCtn, text = 'Contraseña Actual')
entryA = tk.Entry(master = contraseñaCtn)

labelB = tk.Label(master = contraseñaCtn, text = 'Nueva Contraseña')
entryB = tk.Entry(master = contraseñaCtn)

labelC = tk.Label(master = contraseñaCtn, text = 'Confirmar Nueva contraseña')
entryC = tk.Entry(master = contraseñaCtn)

contraseñaBtn = tk.Button(master = contraseñaCtn, text = 'Actualizar')

labelA.pack(pady = 8, padx = 20)
entryA.pack(pady = 8, padx = 20)
labelB.pack(pady = 8, padx = 20)
entryB.pack(pady = 8, padx = 20)
labelC.pack(pady = 8, padx = 20)
entryC.pack(pady = 8, padx = 20)
contraseñaBtn.pack(pady = 20, padx = 20)






vista.mainloop()