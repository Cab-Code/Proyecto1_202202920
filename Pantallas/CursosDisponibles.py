import tkinter as tk
import tkinter.font as tkFont
import sys
import subprocess

carnet = sys.argv[1]
vista = tk.Tk()
vista.title('Cursos Disponibles')
vista.geometry('800x600+0+0')

frame = tk.Frame(vista)
frame.pack(fill='both', expand=True)
canvas = tk.Canvas(frame)
canvas.pack(side='left', fill='both', expand=True)
scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_canvas_configure)

def on_canvas_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind("<MouseWheel>", on_canvas_scroll)


tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)

cursosData = []
cursos = []

MainCtn = tk.Frame(master = vista, padx = 10)
MainCtn.pack()
ib = 0
botonesAsig = []
botonesDesa = []
alumnoDatos = []
alumnoCursos = []


with open('Pantallas/Datos/Cursos/Disponibles.txt') as BaseDatos:
    lectura = BaseDatos.read()
    cursosData = lectura.split('\n')
    print(cursosData)
with open(F'Pantallas/Datos/Alumnos/{carnet}.txt') as AlumnoBaseDatos:
    lectura = AlumnoBaseDatos.read()
    alumnoData = lectura.split('///\n')
    alumnoDatos = alumnoData[0]
    alumnoCursos = alumnoData[1]
    alumnoCursos = alumnoCursos.split('\n')

def rescribir(arg):
    cursDt = arg.split(',') 
    print('-------------------------')
    print(cursDt)
    print('-------------------------')

    with open(F'Pantallas/Datos/Cursos/{cursDt[0]}.txt', 'a') as Intu:
        Intu.write(F'\n{carnet}:0')
    NewData = []
    NalumnoCursos = '\n'.join(alumnoCursos)
    NewData.append(alumnoDatos)
    NewData.append('///\n')
    NewData.append(NalumnoCursos)
    NewData = ''.join(NewData)
    print(NewData)
    with open(F'Pantallas/Datos/Alumnos/{carnet}.txt','w') as AlumnoBaseDatos:
        AlumnoBaseDatos.write(NewData)
    with open(F'Pantallas/Datos/Cursos/Disponibles.txt','w') as DisponiblesDatos:
        NewDataCurso = '\n'.join(cursosData)
        DisponiblesDatos.write(NewDataCurso)
    subprocess.run(['python', 'Pantallas/error.py','Asignacion existosa', 'Asignacion Existosa. Reinicia tu perfil para ver los cambios'])
    


def asignar(i):
    if len(alumnoCursos) < 12:
        alumnoCursos.append(F'{cursos[i]}:0')
        botonesAsig[i]['state'] = tk.DISABLED
        print(alumnoCursos)
        aux = cursosData[i].split(',')
        aux[3] = int(aux[3]) - 1
        aux[3] = str(aux[3])
         
        print(cursosData[i])

        cursosData[i] = ','.join(aux)

        print(cursosData[i])

        rescribir(cursosData[i])
        
    else:
        subprocess.run(['python', 'Pantallas/error.py','Error de asignacion', 'El estudiante no se puede asignar mas de 12 cursos por semestre'])

def desasignar(name):
    i = 0
    for curso in alumnoCursos:
        if curso == name:
            return
        i+=1
    del alumnoCursos[i]
    aux = cursosData[i].split(',')
    aux[3] = int(aux[3]) + 1
    aux[3] = str(aux[3])

    print(cursosData[i])

    cursosData[i] = ','.join(aux)
    print(alumnoCursos)


for curso in cursosData:
    if curso != '':
        curso = curso.split(',')
        cursos.append(curso[0])
        Contenedor = tk.Frame(master = MainCtn, pady = 10, relief = 'solid', borderwidth = 1, padx = 5)
        nCurso = tk.Label(master = Contenedor, text = curso[0], font = tituloFont,width = 20)
        nPrf = tk.Label(master = Contenedor, text = curso[2], font = textoFont)
        asignarBtn = tk.Button(master = Contenedor, text = 'asignar', state = tk.NORMAL, command = lambda k = ib: asignar(k))
        desasignarBtn = tk.Button(master = Contenedor, text = 'desasignar', state = tk.DISABLED, command = lambda k = curso[0]: desasignar(k))
        botonesAsig.append(asignarBtn)
        botonesDesa.append(desasignarBtn)
        for aCurso in  alumnoCursos:
            aCurso = aCurso.split(':')
            if curso[0] == aCurso[0]:
                asignarBtn['state'] = tk.DISABLED
                desasignarBtn['state'] = tk.NORMAL
                break
            if curso[3] == '0':
                asignarBtn['state'] = tk.DISABLED
                desasignarBtn['state'] = tk.DISABLED
                break
        Contenedor.grid(column = 0, row = ib, pady = 5)
        nCurso.grid(column = 0, row = 0)
        nPrf.grid(column = 0, row = 1)
        asignarBtn.grid(column = 1, row = 1, padx = 5)
        desasignarBtn.grid(column = 2, row = 1, padx = 5)
        ib = ib + 1
canvas.create_window((0, 0), window=MainCtn, anchor='nw')

vista.mainloop()