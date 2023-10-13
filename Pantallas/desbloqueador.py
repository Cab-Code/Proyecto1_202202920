import tkinter.font as tkFont
import sys
import subprocess
import tkinter as tk

vista = tk.Tk()
vista.geometry('700x500')

tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)


frame = tk.Frame(vista)
frame.pack(fill='both', expand=True)
canvas = tk.Canvas(frame)
canvas.pack(side='left', fill='both', expand = True)
scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_canvas_configure)

def on_canvas_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind("<MouseWheel>", on_canvas_scroll)

mainCtn = tk.Frame(vista, padx = 10, pady = 10)
mainCtn.pack()
alumnosText = tk.Label(mainCtn, text = '-   Alumnos Bloqueados', font = tituloFont)
alumnosText.pack(pady = 15)

alumnosArray = []
ProfesoresArray = []


def desbloquearAlm(carnet):
    print(carnet)
    DataMain = []
    with open(F'Pantallas/Datos/Alumnos/{carnet}.txt') as ReadCarnet:
        lectura = ReadCarnet.read()
        DataMain = lectura.split(',')
        DataMain[9] = '0///'
        DataWrite = ','.join(DataMain)
        print(DataWrite)
    
    with open(F'Pantallas/Datos/Alumnos/{carnet}.txt', 'w') as WriteData:
        WriteData.write(DataWrite)

def desbloquearPrf(carnet):
    print(carnet)
    DataMain = []
    with open(F'Pantallas/Datos/Profesores/{carnet}.txt') as ReadCarnet:
        lectura = ReadCarnet.read()
        DataMain = lectura.split(',')
        DataMain[7] = '0///'
        DataWrite = ','.join(DataMain)
        print(DataWrite)
    
    with open(F'Pantallas/Datos/Profesores/{carnet}.txt', 'w') as WriteData:
        WriteData.write(DataWrite)


with open('Pantallas/carnets.txt') as carnetsData:
    lectura = carnetsData.read()
    alumnosArray = lectura.split('\n')
    for alumn in alumnosArray:
        with open(F'Pantallas/Datos/Alumnos/{alumn}.txt') as alumnData:
            leer = alumnData.read()
            alumnDataArr = leer.split('///\n')
            alumnDataArr = alumnDataArr[0] .split(',')
            print(alumnDataArr[9])
            Bloq = alumnDataArr[9].split('///')
            if int(Bloq[0]) >= 3:
                Contenedor = tk.Label(mainCtn, padx = 5, pady = 10, relief = 'solid', borderwidth = 1)
                Contenedor.pack(pady = 15)
                carnetLbl = tk.Label(Contenedor, text = alumn, font = tituloFont, padx = 10, width = 10)
                carnetLbl.grid(row = 0, column = 1, pady = 20)
                nombreLbl = tk.Label(Contenedor, text = alumnDataArr[6], font = textoFont, padx = 10, width = 25)
                nombreLbl.grid(row = 0, column = 2)
                desbloqBtn = tk.Button(Contenedor, text = 'desbloquear', font = textoFont, command = lambda k = alumnDataArr[0]: desbloquearAlm(k))
                desbloqBtn.grid(row = 0, column = 3, padx = 10)

catText = tk.Label(mainCtn, text = '-   Catedraticos Bloqueados', font = tituloFont)
catText.pack(pady = 30)


with open('Pantallas/profesores.txt') as pData:
    lectura = pData.read()
    ProfesoresArray = lectura.split('\n')
    for prf in ProfesoresArray:
        with open(F'Pantallas/Datos/Profesores/{prf}.txt') as prfData:
            leer = prfData.read()
            prfDataArr = leer.split('///\n')
            prfDataArr = prfDataArr[0] .split(',')
            print(prfDataArr[7])
            Bloq = prfDataArr[7].split('///')
            if int(Bloq[0]) >= 3:
                Contenedor = tk.Label(mainCtn, padx = 5, pady = 10, relief = 'solid', borderwidth = 1)
                Contenedor.pack(pady = 15)
                carnetLbl = tk.Label(Contenedor, text = prf, font = tituloFont, padx = 10)
                carnetLbl.grid(row = 0, column = 1, pady = 20)
                nombreLbl = tk.Label(Contenedor, text = prfDataArr[5], font = textoFont, padx = 10, width = 20)
                nombreLbl.grid(row = 0, column = 2)
                desbloqBtn = tk.Button(Contenedor, text = 'desbloquear', font = textoFont, command = lambda k = prfDataArr[0]: desbloquearPrf(k))
                desbloqBtn.grid(row = 0, column = 3, padx = 10)



canvas.create_window((0, 0), window= mainCtn, anchor='nw')

vista.mainloop()