import tkinter as tk
import subprocess
import sys
argumentos = sys.argv
colorDos = '#9dc09d'
colorUno = '#9dc09d'

datos = []
cursos = []
carnet = argumentos[len(argumentos) - 1]
BaseDatos = F'Pantallas/Datos/Alumnos/{carnet}.txt'


with open(BaseDatos) as data:
    DataRead = data.read()
    alumno = DataRead.split('///\n')
    print(alumno)
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
vista. geometry('800x600+0+0')

def abrirCurso(curso):
    enlace = F'Pantallas/Datos/Cursos/{curso}.txt'
    print(enlace)

def inicio():
    inicioCtn = tk.Frame(master = vista)
    inicioCtn['bg'] = '#9dc09d'
    datos = tk.Label(master = inicioCtn, text = F"carnet: {carnet}     DPI:{Dpi} \n\n {nombre} {apelli}       {fecha} \n\nusuario: {username}        {correo}")
    datos['bg'] = '#9dc09d'
    inicioCtn.pack(pady = 10)
    datos.pack(padx = 10)


def vistaCursos ():
    cursosCtn = tk.Frame(master = vista)
    text = tk.Label(master = vista, text = 'Cursos Actuales')
    text.pack(pady = 20)
    cursosCtn.pack(pady = 20)
    botones = []
    parametrosBoton = []
    for curso in cursos:
        dataCurso = curso.split(':')
        print(curso)
        botonCurso = tk.Button(master = cursosCtn, text = dataCurso[0], command = lambda parametro = dataCurso[0]: abrirCurso(parametro))
        botones.append(botonCurso)
    i = 0
    j = 0
    for boton in botones:
        print(boton)
        boton.grid(column = i, row = j, padx = 30, pady = 20)
        i+=1
        if i >= 4:
            j+=1
            i = 0

inicio()
vistaCursos()
vista.mainloop()