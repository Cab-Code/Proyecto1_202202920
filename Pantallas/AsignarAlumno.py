import tkinter as tk
import tkinter.font as tkFont
import subprocess



vista = tk.Tk()
vista.geometry('600x625+0+0')
vista.title('Asignar Alumno')

tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)

carnets = []
NewAlumnoData = [100]
NuevoCarnet = 0
def generarCarnet():
    subprocess.run(['Pantallas/OrdenadorCarnets.exe'])
    with open('Pantallas/carnets.txt') as file:
        leer = file.read()
        carnets = leer.split('\n')
        lastCarnet = carnets[-1]
        print(lastCarnet)
        NewCarnet = int(lastCarnet) + 1
        return NewCarnet, carnets

NuevoCarnet, carnets = generarCarnet()

def crearDocumento():
    open(F"Pantallas/Datos/Alumnos/{NuevoCarnet}.txt", 'w').close()


mainCtn = tk.Frame(master = vista)
mainCtn.pack(padx = 5, pady = 20)

titulo = tk.Label(mainCtn, text = 'Ingrese Sus Datos', font =  tituloFont)
titulo.grid(row = 0, column = 0)

carnetLbl = tk.Label(mainCtn, text = F'Carnet: {NuevoCarnet}', font =  textoFont)
carnetLbl.grid(row = 1, column = 0, pady = 20)


DpiLbl = tk.Label(mainCtn, text = 'DPI', font =  textoFont)
DpiLbl.grid(row = 2, column = 0)
DpiEnt = tk.Entry(mainCtn, font =  textoFont)
DpiEnt.grid(row = 3, column = 0)

nombreLbl = tk.Label(mainCtn, text = 'Nombres', font =  textoFont)
nombreLbl.grid(row = 4, column = 0)
nombreEnt = tk.Entry(mainCtn, font =  textoFont)
nombreEnt.grid(row = 5, column = 0)

apellidoLbl = tk.Label(mainCtn, text = 'Apellidos', font =  textoFont)
apellidoLbl.grid(row = 6, column = 0)
apellidoEnt = tk.Entry(mainCtn, font =  textoFont)
apellidoEnt.grid(row = 7, column = 0)

subCtn = tk.Frame(vista, padx = 5, pady = 5)
subCtn.pack(pady = 20)

firstCtn = tk.Frame(subCtn, padx = 5, pady = 5)
firstCtn.grid(row = 0, column = 0, padx = 20)

fnLbl = tk.Label(firstCtn, text = 'Fecha de Nacimiento\n DD/MM/AAAA', pady = 5)
fnLbl.grid(row = 0, column = 0)
fnEnt = tk.Entry(firstCtn)
fnEnt.grid(row = 1, column = 0, padx = 5)

SecondCtn = tk.Frame(subCtn, padx = 5, pady = 5)
SecondCtn.grid(row = 0, column = 1, padx = 20)

secLbl = tk.Label(SecondCtn, text = 'Telefono\n', pady = 5)
secLbl.grid(row = 0, column = 0)
telEntry = tk.Entry(SecondCtn)
telEntry.grid(row = 1, column = 0)

trdCtn = tk.Frame(subCtn, padx = 5, pady = 5)
trdCtn.grid(row = 0, column = 2, padx = 20)

trdLbl = tk.Label(trdCtn, text = 'Correo Electronico\n', pady = 5)
trdLbl.grid(row = 0, column = 0)
correoEntry = tk.Entry(trdCtn)
correoEntry.grid(row = 1, column = 0)


crdCtn = tk.Frame(vista, padx = 5, pady = 5)
crdCtn.pack()

crdLbl = tk.Label(crdCtn, text = 'Contraseña', pady = 5)
crdLbl.pack()
contraN1Entry = tk.Entry(crdCtn)
contraN1Entry.pack()
confirmar = tk.Label(crdCtn, text = 'Confirmar Contraseña', pady = 5)
confirmar.pack()
contraN2Entry = tk.Entry(crdCtn)
contraN2Entry.pack()


def validarContra():
    contraA = contraN1Entry.get()
    contraB = contraN2Entry.get()

    vMay = False
    vMin = False
    vsimb = False

    if len(contraA) >= 8:
        for char in contraA:
            char = ord(char)
            if char >= 32 and char <= 47:
                vSimb = 1
            if char > 47 and char <= 57:
                vNum = 1
            if char >= 65 and char <= 90:
                vMay = 1
            if char >= 97 and char <= 122:
                vMin = 1
            print(char)
        if vSimb == 1 and vNum == 1 and vMay == 1 and vMin == 1:
            if contraA == contraB:
                print('Contra Validaaaa')
                print(NewAlumnoData)
            else:
                subprocess.run(['python', 'Pantallas/error.py', 'Datos Incorrectos', 'Confirme su contraseña'])

    else:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos Incorrectos', 'Su contraseña debe tener: Mayusculas, Minusculas\n Minimo un numero y un simbolo [  !, ", #, $, %, &, /,), (, *, +, -, ·	]'])


def validarCorreo():
    correo = correoEntry.get()
    valid = 0
    v = 0
    for letra in correo:
        if letra == '@':
            valid = 1
        if letra == '.' and valid == 1:
            v = 4
               
    if v == 4:
        print('Correo valido') 
        validarContra() 
    else:   
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'ingrese un correo electronico valido (ejemplo: userName@gmail.com)'])


def validarTel():
    telString = telEntry.get()
    validTel = False
    if len(telString) == 8:
        print('correcto')
        try:
            aux = int(telString)
            validTel = True
        except:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'En el area Tel Ingrese solo datos numericos'])

    else:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El numero de telefono debe tener 8 digitos'])
    if validTel:
        NewAlumnoData.append(telString)
        validarCorreo()

def validarFecha():
    fechaString = fnEnt.get()
    fechaLista = fechaString.split('/')
    if len(fechaLista) == 3:
        for dato in fechaLista:
            try:
                aux = int(dato)
            except:
                subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El formato de fecha es incorrecto (DD/MM/AAAA)'])
        if int(fechaLista[0]) >= 0 and int(fechaLista[0]) < 31:
            if int(fechaLista[1]) > 0 and int(fechaLista[1]) <= 12:
                if int(fechaLista[2]) > 1920 and int(fechaLista[2]) < 2006:
                    NewAlumnoData.append(fechaString)
                    validarTel()
    else:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El formato de fecha es incorrecto (DD/MM/AAAA)'])


def validarDPI():
    dpi = DpiEnt.get()
    validDpi = True
    try:
        NumDpi = int(dpi)
        if len(dpi) != 13:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El DPI debe ser un dato numerico de 13 digitos'])
    except:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El DPI debe ser un dato numerico de 13 digitos'])
    for carnet in carnets:
        print(carnet)
        with open(F'Pantallas/Datos/Alumnos/{carnet}.txt') as carnetData:
            leer = carnetData.read()
            alumnoData = leer.split(',')
            if dpi == alumnoData[3]:
                validarDPI = False
                subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'Este DPI ya ha sido registrado (Usted podria estar cometiendo suplantacion de identidad)']) 
                break
            print(alumnoData[3])
    if validDpi:
        nombre = nombreEnt.get()
        apellido = apellidoEnt.get()

        if nombre != '' and apellido != '':
            NewAlumnoData.append(NuevoCarnet) 
            NewAlumnoData.append(nombre)
            NewAlumnoData.append(apellido)
            NewAlumnoData.append(dpi)
            validarFecha()
        else:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'Igrese su nombre y apellidos'])

        


asignarBtn = tk.Button(vista, text = 'asignar', command = validarDPI, relief = 'solid', borderwidth = 1)
asignarBtn.pack(pady = 30)



vista.mainloop()