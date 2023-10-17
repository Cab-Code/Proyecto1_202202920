import tkinter as tk
import tkinter.font as tkFont
import subprocess
from PIL import ImageTk, Image
import sys

argumentosPrograma = sys.argv

vista = tk.Tk()
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
nameCurso = str(argumentosPrograma[1])
carnet = str(argumentosPrograma[2])

curso = []


vista.title(F'{nameCurso} {carnet}')
vista.geometry('600x600+20+20')

with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt') as BaseDatos:
    lectura = BaseDatos.read()
    curso = lectura.split('///\n')

titulo = curso[0]
descripcion = curso[1]
imgCurso = curso[3]
profesor = curso[2]

bannerImg = ImageTk.PhotoImage(Image.open(F'Pantallas/Datos/Imagenes/{imgCurso}.jpg'))
banner = tk.Label(master = vista, image = bannerImg, height = 150)
tituloVs = tk.Label(master = vista, font = tituloFont, text = titulo)
descripcionVs = tk.Label(master = vista, font = textoFont, text = descripcion)
banner.pack()
tituloVs.pack(pady = 20)
descripcionVs.pack()
prfDatos = []
with open(F'Pantallas/Datos/Profesores/{profesor}.txt') as profesorDB:
    leer = profesorDB.read()
    prfDatos = leer.split(',')

prfesor = tk.Label(master = vista, text = F'Catedratico: {prfDatos[1]} {prfDatos[2]}')
prfesor.pack(pady = 10)

almDatos = []
almCursos = []
almPostCursos = []
with open(F'Pantallas/Datos/Alumnos/{carnet}.txt') as alumnoDB:
    leer = alumnoDB.read()
    almDatos = leer.split('///\n')
    almCursos = almDatos[1].split('\n')
    print(almCursos)
for curso in almCursos:
    cursoSplit = curso.split(':')
    almPostCursos.append(cursoSplit)

i = 0
for curso in almPostCursos:
    if curso[0] == nameCurso:
        print(i)
    i+=1

almNotaFCursos =['']

with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt') as CursoFileR:
    leer = CursoFileR.read()
    CrsData = leer.split('///\n')
    AlmnsCrs = CrsData[4].split('\n')
    print(AlmnsCrs)

    for alumno in AlmnsCrs:
        DatAlumno = alumno.split(':')
        DatAlumno
        if  carnet == DatAlumno[0]:
            almNotaFCursos[0] = DatAlumno[1]
            break
        else:
            almNotaFCursos[0] = DatAlumno[1]


EstudianteNotaC = tk.Label(master = vista, text = F'{carnet}\n\n Nota: {almNotaFCursos[0]}/100 pts', font = tituloFont)
EstudianteNotaC.pack(pady = 10)



vista.mainloop()