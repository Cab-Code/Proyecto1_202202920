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

BaseDatos = F'Pantallas/Datos/Profesores/{carnet}.txt'


with open(BaseDatos) as data:
    DataRead = data.read()
    alumno = DataRead.split('///\n')
    datos = alumno[0].split(',')
    cursos = alumno[1].split('\n')

nombre= datos[1]
apelli = datos[2]
tel = datos[3]
correo = datos[4]
username = datos[5]
contra = datos[6]



vista = tk.Tk()
vista.title('Catedratico')
vista. geometry('1000x655+0+0')
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
interCt = tk.Frame(master = vista)
interCt.pack()

def cerrarSecion():
    vista.destroy()
    subprocess.run(['python', '..\Proyecto/Main.py'])
    

def usuarioConfig():
    subprocess.run(['python', 'Pantallas/configPrf.py', carnet])
    

def abrirCurso(curso):
    enlace = F'Pantallas/CursoVistaProfesor.py'
    print(curso)
    subprocess.run(['python', enlace,curso, carnet])

def inicio():
    r0c0 = tk.Frame(master = interCt, cursor = 'hand2')
    r0c0['bg'] = colorUno
    userText = tk.Button(master = r0c0, text = F"Profesor: {nombre} {apelli} \n\n DPI: {carnet}", command = usuarioConfig, width = 100, pady = 30, font = textoFont, borderwidth=1, relief="solid")
    r0c0.grid(row = 0, column = 0, sticky = 'W')
    userText.pack()

def vistaCursos ():
    
    cursosCtn = tk.Frame(master = interCt)
    botonesCtn = tk.Frame(master = cursosCtn)
    text = tk.Label(master = cursosCtn, text = 'Cursos', font = tituloFont)
    text.grid(column = 0, row = 0)
    botonesCtn.grid(column = 0, row = 1)
    cursosCtn.grid(pady = 20, row = 1, column = 0)
    extLabel = tk.Label(master = cursosCtn, text = " ")
    extLabel.grid(column = 1, row = 0, pady = 20)
    botones = []
    for curso in cursos:
        dataCurso = curso.split(':')
        botonCurso = tk.Button(master = botonesCtn, text = dataCurso[0], command = lambda parametro = dataCurso[0]: abrirCurso(parametro), borderwidth=1, relief="solid", pady = 20, width = 20, cursor = 'hand2')
        botones.append(botonCurso)
    i = 0
    j = 0
    for boton in botones:
        boton.grid(column = i, row = j, padx = 15, pady = 20)
        i+=1
        if i >= 4:
            j+=1
            i = 0

    cerrarSecionBtn = tk.Button(master = cursosCtn, text = 'Cerrar Secion', command = cerrarSecion, font = textoFont, borderwidth=1, relief="solid", cursor = 'hand2')
    cerrarSecionBtn.grid(row = 2, column = 1)




inicio()
vistaCursos()
vista.mainloop()