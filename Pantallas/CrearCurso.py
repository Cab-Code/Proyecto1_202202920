import tkinter as tk
import tkinter.font as tkFont
import subprocess


NewCurso = ['', '', '', '']


vista = tk.Tk()
vista.title('Administrador')
vista.geometry('800x400+50+50')
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
texto = tk.Label(vista, text = 'Administrador', font = tituloFont)
texto.pack()
mainCtn = tk.Frame(vista)
mainCtn.pack()
textoI = tk.Label(mainCtn, text = 'Ingrese los datos del curso', font = tituloFont)
textoI.pack(pady = 50)

dataCtn = tk.Frame(mainCtn)
dataCtn.pack()

NombreTxt = tk.Label(dataCtn, text = 'Nombre curso', font = textoFont)
NombreTxt.grid(column = 0, row = 0, padx = 10)

NombreEntry = tk.Entry(dataCtn)
NombreEntry.grid(column = 0, row = 1, padx = 10)

DpiTxt = tk.Label(dataCtn, text = 'DPI del catedratico', font = textoFont)
DpiTxt.grid(column = 1, row = 0, padx = 10)

DpiEntry = tk.Entry(dataCtn)
DpiEntry.grid(column = 1, row = 1, padx = 10)

PrfTxt = tk.Label(dataCtn, text = 'Nombre del catedratico', font = textoFont)
PrfTxt.grid(column = 2, row = 0, padx = 10)

PrfEntry = tk.Entry(dataCtn)
PrfEntry.grid(column = 2, row = 1, padx = 10)

cupoTxt = tk.Label(dataCtn, text = 'Cupo del curso', font = textoFont)
cupoTxt.grid(column = 3, row = 0, padx = 10)

cupoEntry = tk.Entry(dataCtn)
cupoEntry.grid(column = 3, row = 1, padx = 10)



def escribir():
    with open('Pantallas/Datos/Cursos/Disponibles.txt', 'a') as DispFile:
        NewData = ','.join(NewCurso)
        print(NewData)
        DispFile.write(F'\n{NewData}')
    with open(F'Pantallas/Datos/Profesores/{NewCurso[1]}.txt', 'a') as PrfFile:
        PrfFile.write(F'\n{NewCurso[0]}')    
    open(F'Pantallas/Datos/Cursos/{NewCurso[0]}.txt', 'w').close()

    with open(F'Pantallas/Datos/Cursos/{NewCurso[0]}.txt', 'w') as FileNewCurso:
         FileNewCurso.write(F'titulo///\nEsta es la descripcion del curso///\n{NewCurso[1]}///\nimg0///')
    

def validarCupo():
    cupo = cupoEntry.get()
    print(NewCurso)
    print(cupo)
    try:
        aus = int(cupo)
        NewCurso[3] = cupo
        print(NewCurso)
        escribir()
        
    except:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El cupo del curso debe ser un numero entero'])


def validarDpi():
    validDpi = False
    dpi = DpiEntry.get()
    if len(dpi) == 13:
        try:
            aux = int(dpi)
        except:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'Ingrese un DPI valido'])
        with open('Pantallas/profesores.txt') as filePrf:
            leer = filePrf.read()
            dpis = leer.split('\n')


            for d in dpis:
                print(d)
                if d == dpi:
                     validDpi = True
            if validDpi:
                NewCurso[1]  = dpi
                NewCurso[2] = PrfEntry.get()
                validarCupo()   
            else:
                subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El DPI ingresado no esta asociado a ningun profesor'])
                     
                    

            
             

def validarNombre():
    nombre = NombreEntry.get()
    if len(nombre) > 0 and len(nombre) < 22:
        print(nombre)
        NewCurso[0] = nombre
        validarDpi()
    else:
            subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'El nombre del curso tiene un maximo de 22 caracteres'])





crearBtn = tk.Button(mainCtn, text = 'Crear Curso', command = validarNombre)
crearBtn.pack(pady = 50)

vista.mainloop()