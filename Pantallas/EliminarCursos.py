import tkinter as tk
import tkinter.font as tkFont
import sys
import os
import subprocess

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

botonesDesa = []



with open('Pantallas/Datos/Cursos/Disponibles.txt') as BaseDatos:
    lectura = BaseDatos.read()
    cursosData = lectura.split('\n')
    print(cursosData)


def rescribir():

    with open(F'Pantallas/Datos/Cursos/Disponibles.txt','w') as DisponiblesDatos:
        NewDataCurso = '\n'.join(cursosData)
        DisponiblesDatos.write(NewDataCurso)
    subprocess.run(['python', 'Pantallas/error.py','Asignacion existosa', 'Asignacion Existosa. Reinicia tu perfil para ver los cambios'])
    vista.destroy()


def eliminar(name):
    os.remove(F'Pantallas/Datos/Cursos/{name}.txt')
    i = 0
    for cursos in cursosData:
        Crs = cursos.split(',')
        if name == Crs[0]:
            print(i)
            break
        i += 1
    aux = cursosData[i]
    botonesDesa[i]['state'] = tk.DISABLED
    cursosData[i] = cursosData[len(cursosData)-1]
    cursosData[len(cursosData)-1] = aux
    cursosData.pop(-1)
    final = '\n'.join(cursosData)

    print(final)
    rescribir()


for curso in cursosData:
    if curso != '':
        curso = curso.split(',')
        cursos.append(curso[0])
        Contenedor = tk.Frame(master = MainCtn, pady = 10, relief = 'solid', borderwidth = 1, padx = 5)
        nCurso = tk.Label(master = Contenedor, text = curso[0], font = tituloFont,width = 20)
        nPrf = tk.Label(master = Contenedor, text = curso[2], font = textoFont)
        desasignarBtn = tk.Button(master = Contenedor, text = 'Eliminar', state = tk.NORMAL, command = lambda k = curso[0]: eliminar(k))
        botonesDesa.append(desasignarBtn)
        
        Contenedor.grid(column = 0, row = ib, pady = 5)
        nCurso.grid(column = 0, row = 0)
        nPrf.grid(column = 0, row = 1)
        desasignarBtn.grid(column = 2, row = 1, padx = 5)
        ib = ib + 1
canvas.create_window((0, 0), window=MainCtn, anchor='nw')

vista.mainloop()