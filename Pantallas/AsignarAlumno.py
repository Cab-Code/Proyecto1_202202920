import tkinter as tk
import tkinter.font as tkFont



vista = tk.Tk()
vista.geometry('600x600+0+0')
vista.title('Asignar Alumno')

tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)

NuevoCarnet = 0

def CrearCarnet():
    print('Carnet')

def crearDocumento():
    archivo = open('Pantallas/Datos/Alumnos/prueba.txt', 'w')
    archivo.write('Hola Mundo')







mainCtn = tk.Frame(master = vista)
mainCtn.pack(padx = 5, pady = 20)

titulo = tk.Label(mainCtn, text = 'Ingrese Sus Datos', font =  tituloFont)
titulo.grid(row = 0, column = 0)

DpiLbl = tk.Label(mainCtn, text = 'DPI', font =  textoFont)
DpiLbl.grid(row = 1, column = 0)
DpiEnt = tk.Entry(mainCtn, font =  textoFont)
DpiEnt.grid(row = 2, column = 0)

nombreLbl = tk.Label(mainCtn, text = 'Nombres', font =  textoFont)
nombreLbl.grid(row = 3, column = 0)
nombreEnt = tk.Entry(mainCtn, font =  textoFont)
nombreEnt.grid(row = 4, column = 0)

apellidoLbl = tk.Label(mainCtn, text = 'Apellidos', font =  textoFont)
apellidoLbl.grid(row = 5, column = 0)
apellidoEnt = tk.Entry(mainCtn, font =  textoFont)
apellidoEnt.grid(row = 6, column = 0)

subCtn = tk.Frame(vista, padx = 5, pady = 5)
subCtn.pack(pady = 20)

firstCtn = tk.Frame(subCtn, padx = 5, pady = 5)
firstCtn.grid(row = 0, column = 0, padx = 20)

fnLbl = tk.Label(firstCtn, text = 'Fecha de Nacimiento\n DD/MM/AAAA', pady = 5)
fnLbl.grid(row = 0, column = 0)
fnDiaEnt = tk.Entry(firstCtn)
fnDiaEnt.grid(row = 1, column = 0, padx = 5)

SecondCtn = tk.Frame(subCtn, padx = 5, pady = 5)
SecondCtn.grid(row = 0, column = 1, padx = 20)

secLbl = tk.Label(SecondCtn, text = 'Telefono\n', pady = 5)
secLbl.grid(row = 0, column = 0)
telEntry = tk.Entry(SecondCtn)
telEntry.grid(row = 1, column = 0)

trdCtn = tk.Frame(subCtn, padx = 5, pady = 5)
trdCtn.grid(row = 0, column = 2, padx = 20)

trdLbl = tk.Label(trdCtn, text = 'Correo Electronico\n', pady = 5)
trdLbl.grid(row = 0, column = 0)
correoEntry = tk.Entry(trdCtn)
correoEntry.grid(row = 1, column = 0)


crdCtn = tk.Frame(vista, padx = 5, pady = 5)
crdCtn.pack()

crdLbl = tk.Label(crdCtn, text = 'Contraseña', pady = 5)
crdLbl.pack()
contraN1Entry = tk.Entry(crdCtn)
contraN1Entry.pack()
confirmar = tk.Label(crdCtn, text = 'Confirmar Contraseña', pady = 5)
confirmar.pack()
contraN2Entry = tk.Entry(crdCtn)
contraN2Entry.pack()

asignarBtn = tk.Button(vista, text = 'asignar')
asignarBtn.pack()

crearDocumento()

vista.mainloop()