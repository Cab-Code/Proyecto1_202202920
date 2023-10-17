import tkinter as tk
import tkinter.font as tkFont
import subprocess
import sys

vista = tk.Tk()
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
nameCurso = sys.argv[1]
carnet = sys.argv[2]
vista.title(F'{nameCurso}')
vista.geometry('400x100+20+20')

AlumnosData = []
CursoData = []

with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt') as FileCurso:
    lectura = FileCurso.read()
    CursoData = lectura.split('///\n')
    AlumnosData = CursoData[4]
    AlumnosData = AlumnosData.split('\n')

mainCtn = tk.Frame(vista)
mainCtn.pack()

txt = tk.Label(mainCtn, text = F'{carnet}: ', font = tituloFont)
txt.grid(column = 0, row = 0, pady = 10)
entry = tk.Entry(mainCtn)
entry.grid(column = 2, row = 0, pady = 10)

NewData = []

def cambiar_Nota():
    newNota = entry.get()
    aux = 0
    print(carnet)
    i = 0
    alumni = ''
    try:
        aux = int(newNota)
        for alumno in AlumnosData:
            alm = alumno.split(':')
            if alm[0] == carnet:
                print(alm)
                if aux > 0 and aux <= 100:
                    alm[1] = newNota
                    print(alumni)
                    alumni = ':'.join(alm)
                    print(alumni)
                    alumno = alumni
                    AlumnosData[i] = alumni
                    print(AlumnosData)
                    CursoData[4] = '\n'.join(AlumnosData)
                    NewData = '///\n'.join(CursoData)
                    print(NewData)
                    with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt', 'w') as FileW:
                        FileW.write(NewData)


            i += 1
    except:
        subprocess.run(['python', 'Pantallas/error.py', 'Datos incorrectos', 'Ingrese un numero entero'])

    print(AlumnosData)



Btn = tk.Button(mainCtn, text = 'Guardar', command = cambiar_Nota)
Btn.grid(column = 1, row = 1, pady = 10)




vista.mainloop()