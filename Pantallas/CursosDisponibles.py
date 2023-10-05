import tkinter as tk
import tkinter.font as tkFont
import sys

carnet = sys.argv[1]
vista = tk.Tk()
vista.title('Cursos Disponibles')
vista.geometry('800x600+0+0')

tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)

cursosData = []
cursos = []

MainCtn = tk.Frame(master = vista, padx = 10)
MainCtn.pack()
ib = 0

alumnoCursos = []

with open('Pantallas/Datos/Cursos/Disponibles.txt') as BaseDatos:
    lectura = BaseDatos.read()
    cursosData = lectura.split('\n')
    print(cursosData)
with open(F'Pantallas/Datos/Alumnos/{carnet}.txt') as AlumnoBaseDatos:
    lectura = AlumnoBaseDatos.read()
    alumnoData = lectura.split('///\n')
    alumnoCursos = alumnoData[1]
    alumnoCursos = alumnoCursos.split('\n')

for curso in cursosData:
    if curso != '':
        curso = curso.split(',')
        Contenedor = tk.Frame(master = MainCtn, pady = 10, relief = 'solid', borderwidth = 1, padx = 5)
        nCurso = tk.Label(master = Contenedor, text = curso[0], font = tituloFont,width = 20)
        nPrf = tk.Label(master = Contenedor, text = curso[2], font = textoFont)
        asignar = tk.Button(master = Contenedor, text = 'asignar', state = tk.NORMAL)
        desasignar = tk.Button(master = Contenedor, text = 'desasignar', state = tk.DISABLED)
        for aCurso in  alumnoCursos:
            aCurso = aCurso.split(':')
            print(curso[0])
            if curso[0] == aCurso[0]:
                asignar['state'] = tk.DISABLED
                desasignar['state'] = tk.NORMAL
                print(aCurso[0])
                break
        Contenedor.grid(column = 0, row = ib, pady = 5)
        nCurso.grid(column = 0, row = 0)
        nPrf.grid(column = 0, row = 1)
        asignar.grid(column = 1, row = 1)
        desasignar.grid(column = 2, row = 1)
        ib = ib + 1



vista.mainloop()