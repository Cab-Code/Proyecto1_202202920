import tkinter as tk
import tkinter.font as tkFont
import subprocess
import sys
argumentos = sys.argv

colorUno = '#fff'
colorDos = '#fff'
colorTres = '#20c67a'

datos = []
cursos = []
carnet = argumentos[len(argumentos) - 1]
print(carnet)
BaseDatos = F'Pantallas/Datos/Alumnos/{carnet}.txt'


with open(BaseDatos) as data:
    DataRead = data.read()
    alumno = DataRead.split('///\n')
    datos = alumno[0].split(',')
    cursos = alumno[1].split('\n')

nombre = datos[1]
apelli = datos[2]
Dpi = datos[3]
fecha = datos[4]
tel = datos[5]
username = datos[6]
correo = datos[7]
contra = datos[8]
estado = datos[9]


vista = tk.Tk()
vista.title('Alumno')
vista. geometry('1000x655+0+0')
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
interCt = tk.Frame(master = vista)
interCt.pack()

def cerrarSecion():
    vista.destroy()
    subprocess.run(['python', '..Proyecto\Main.py'])
    

def masCursos():
    if len(cursos) < 12:
        print('Tienes menos de 12 cursos')
        print(len(cursos))
        subprocess.run(['python','Pantallas/CursosDisponibles.py'])
    else:
        subprocess.run(['python', 'Pantallas/error.py','Sobre Carga De Cursos', 'No puedes asignarte mas de 12 cursos por semestre'])

def usuarioConfig():
    print('mas Cursos')

def abrirCurso(curso):
    enlace = F'Pantallas/Datos/Cursos/{curso}.txt'
    print(enlace)

def inicio():
    r0c0 = tk.Frame(master = interCt, cursor = 'hand2')
    r0c0['bg'] = colorUno
    userConfigBtn = tk.Button(master = r0c0, text = F"carnet: {carnet} \n\nDPI:{Dpi}\n\n{nombre}  {apelli}\n\n DPI:{username}", command = usuarioConfig, width = 100, pady = 30, font = textoFont, relief = 'flat')
    userConfigBtn['bg'] = colorTres
    r0c0.grid(row = 0, column = 0, sticky = 'W')
    userConfigBtn.pack()

def vistaCursos ():
    
    cursosCtn = tk.Frame(master = interCt, bg = colorDos)
    botonesCtn = tk.Frame(master = cursosCtn, bg = colorUno, relief = 'ridge')
    text = tk.Label(master = cursosCtn, text = 'Cursos Actuales', font = tituloFont)
    text.grid(column = 0, row = 0)
    botonesCtn.grid(column = 0, row = 1)
    cursosCtn.grid(pady = 20, row = 1, column = 0)
    extLabel = tk.Label(master = cursosCtn, text = " ")
    extLabel.grid(column = 1, row = 0, pady = 20)
    masCursosBtn = tk.Button(master = cursosCtn, text = 'Mas Cursos...', command = masCursos, font = textoFont)
    masCursosBtn.grid(column = 1, row = 1)
    botones = []
    for curso in cursos:
        dataCurso = curso.split(':')
        botonCurso = tk.Button(master = botonesCtn, text = dataCurso[0], command = lambda parametro = dataCurso[0]: abrirCurso(parametro), relief = 'flat', pady = 20, bg = colorTres, width = 18)
        botones.append(botonCurso)
    i = 0
    j = 0
    for boton in botones:
        boton.grid(column = i, row = j, padx = 30, pady = 20)
        i+=1
        if i >= 4:
            j+=1
            i = 0

    cerrarSecionBtn = tk.Button(master = cursosCtn, text = 'Cerrar Secion', command = cerrarSecion, font = textoFont)
    cerrarSecionBtn.grid(row = 2, column = 1)




inicio()
vistaCursos()
vista.mainloop()