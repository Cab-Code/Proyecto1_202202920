import tkinter as tk
import tkinter.font as tkFont
import subprocess
import bcrypt


salt = b'$2b$12$ASCDyiUrL20F696Dwg8Iw.'

vista = tk.Tk()
vista.geometry('600x625+0+0')
vista.title('Asignar Alumno')

tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)

PrfDPI = ''
profesores = []
NewProfeData = ['', '', '', '', '','', '', '0///']

with open('Pantallas/profesores.txt') as profesFile:
    leer = profesFile.read()
    profesores = leer.split('\n')

userName = ''
def crearDocumento():
    open(F"Pantallas/Datos/Alumnos/{PrfDPI}.txt", 'w').close()


mainCtn = tk.Frame(master = vista)
mainCtn.pack(padx = 5, pady = 20)

titulo = tk.Label(mainCtn, text = 'Ingrese Los Datos Del Catedratico', font =  tituloFont)
titulo.grid(row = 0, column = 0)



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
contraN1Entry = tk.Entry(crdCtn, show = '*')
contraN1Entry.pack()
confirmar = tk.Label(crdCtn, text = 'Confirmar Contraseña', pady = 5)
confirmar.pack()
contraN2Entry = tk.Entry(crdCtn, show = '*')
contraN2Entry.pack()

def escribir():
    NewData = ','.join(NewProfeData)
    print(NewData)
    open(F'Pantallas/Datos/Profesores/{NewProfeData[0]}.txt', 'w').close()

    with open(F'Pantallas/Datos/Profesores/{NewProfeData[0]}.txt', 'w') as ProfeFile:
        ProfeFile.write(NewData)
    
    with open('Pantallas/profesores.txt', 'a') as carnetsFile:
        carnetsFile.write(F'\n{NewProfeData[0]}')

    subprocess.run(['python', 'Pantallas/error.py', 'Asignacion correcta', F'Sus Datos Son:\n DPI: {NewProfeData[0]}      Usuario: {NewProfeData[5]}'])
    vista.destroy()


def validarContra():
    contraA = contraN1Entry.get()
    contraB = contraN2Entry.get()

    vMay = False
    vMin = False
    vSimb = False
    vNum = False

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
                newContra1 = bytes(contraA, 'utf-8')
                NewEncriptedContra = bcrypt.hashpw(newContra1, salt)
                encriptedContra = str(NewEncriptedContra)
                encriptedContra = encriptedContra[2:-1]
                print(encriptedContra)

                NewProfeData[6] = encriptedContra
                print(NewProfeData)

                escribir()
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
        NewProfeData[4] = correo
        validarContra() 
    else:   
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'ingrese un correo electronico valido (ejemplo: userName@gmail.com)'])

def crearUserName():
    nombre = nombreEnt.get().split(' ')
    nombreA = nombre[0]
    apellido = apellidoEnt.get().split(' ')
    apellidoA = apellido[0]

    userName = F'{nombreA} {apellidoA}'
    
    with open('Pantallas/profesores.txt') as prfsDB:
        leer = prfsDB.read()
        prfsComp = leer.split('\n')
        for carnet in prfsComp:
            db = open(F'Pantallas/Datos/Profesores/{carnet}.txt')
            info = db.read()
            carnetInfo = info.split(',')
            if userName == carnetInfo[6]:
                userName = F'{nombreA}_{apellidoA}_{apellido[1]}'
                print(userName)
            db.close()
    print(userName)
    NewProfeData[5] = userName

    validarCorreo()

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
        NewProfeData[3] = telString
        crearUserName()

def validarDPI():
    dpi = DpiEnt.get()
    validDpi = True
    try:
        NumDpi = int(dpi)
        if len(dpi) != 13:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El DPI debe ser un dato numerico de 13 digitos'])
    except:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El DPI debe ser un dato numerico de 13 digitos'])
    for prf in profesores:
        print(prf)

        if prf == dpi:
            validDpi = False
            break
    if validDpi:
        nombre = nombreEnt.get()
        apellido = apellidoEnt.get()

        if nombre != '' and apellido != '':
            NewProfeData[0] = dpi 
            NewProfeData[1] = nombre
            NewProfeData[2] = apellido
            validarTel()
        else:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'Igrese su nombre y apellidos'])

        


asignarBtn = tk.Button(vista, text = 'asignar', command = validarDPI, relief = 'solid', borderwidth = 1)
asignarBtn.pack(pady = 30)



vista.mainloop()