import tkinter as tk
import tkinter.font as tkFont
import subprocess
from PIL import ImageTk, Image
import sys


nameCurso = sys.argv[1]
imgCurso = 'img0'


vista = tk.Tk()
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
vista.geometry('550x600')


def asignarIMG(parm):
    imgCurso = parm
    print(imgCurso)




mainCtn = tk.Frame(vista, padx = 10, pady = 10)
mainCtn.pack()

primerLbl = tk.Label(mainCtn, text = 'Editor de curso')
primerLbl.pack()

descripcionLbl = tk.Label(mainCtn, text = 'Descripcion: ')
descripcionLbl.pack()

descEntry = tk.Text(mainCtn,width = 80, height = 6)
descEntry.pack()

galeria = tk.Frame(mainCtn)
galeria.pack()


def escribir():
    desc = descEntry.get("1.0", "end")
    with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt') as FileDB:
        leer = FileDB.read()
        datos = leer.split('///\n')
        datos[1] = desc
        datos[3] = imgCurso
        print(datos)
        Newdatos = '///\n'.join(datos)
        print(datos)
        with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt', 'w') as FileDBW:
            FileDBW.write(Newdatos)
        

galeriaLbl = tk.Label(galeria, text = 'imagen de curso')
galeriaLbl.grid(column = 1, row = 0)

img1 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img1.jpg'))
img1Btn = tk.Button(master = galeria, image = img1, height = 50, width = 150, command = lambda: asignarIMG('img1'), relief = 'flat')
img1Btn.grid(column = 0, row = 1, padx = 10, pady = 10)

img2 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img2.jpg'))
img2Btn = tk.Button(master = galeria, image = img2, height = 50, width = 150, command = lambda: asignarIMG('img2'), relief = 'flat')
img2Btn.grid(column = 1, row = 1, padx = 10, pady = 10)


img3 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img3.jpg'))
img3Btn = tk.Button(master = galeria, image = img3, height = 50, width = 150, command = lambda: asignarIMG('img3'), relief = 'flat')
img3Btn.grid(column = 2, row = 1, padx = 10, pady = 10)

img4 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img4.jpg'))
img4Btn = tk.Button(master = galeria, image = img4, height = 50, width = 150, command = lambda: asignarIMG('img4'), relief = 'flat')
img4Btn.grid(column = 0, row = 4, padx = 10, pady = 10)

img5 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img5.jpg'))
img5Btn = tk.Button(master = galeria, image = img5, height = 50, width = 150, command = lambda: asignarIMG('img5'), relief = 'flat')
img5Btn.grid(column = 0, row = 3, padx = 10, pady = 10)

img6 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img6.jpg'))
img6Btn = tk.Button(master = galeria, image = img6, height = 50, width = 150, command = lambda: asignarIMG('img6'), relief = 'flat')
img6Btn.grid(column = 0, row = 2, padx = 10, pady = 10)

img7 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img7.jpg'))
img7Btn = tk.Button(master = galeria, image = img7, height = 50, width = 150, command = lambda: asignarIMG('img7'), relief = 'flat')
img7Btn.grid(column = 1, row = 2, padx = 10, pady = 10)

img8 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img8.jpg'))
img8Btn = tk.Button(master = galeria, image = img8, height = 50, width = 150, command = lambda: asignarIMG('img8'), relief = 'flat')
img8Btn.grid(column = 2, row = 2, padx = 10, pady = 10)

img9 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img9.jpg'))
img9Btn = tk.Button(master = galeria, image = img9, height = 50, width = 150, command = lambda: asignarIMG('img9'), relief = 'flat')
img9Btn.grid(column = 1, row = 4, padx = 10, pady = 10)

img10 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img10.jpg'))
img10Btn = tk.Button(master = galeria, image = img10, height = 50, width = 150, command = lambda: asignarIMG('img10'), relief = 'flat')
img10Btn.grid(column = 1, row = 3, padx = 10, pady = 10)

img11 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img11.jpg'))
img11Btn = tk.Button(master = galeria, image = img11, height = 50, width = 150, command = lambda: asignarIMG('img11'), relief = 'flat')
img11Btn.grid(column = 2, row = 3, padx = 10, pady = 10)

img12 = ImageTk.PhotoImage(Image.open('Pantallas/Datos/Imagenes/img12.jpg'))
img12Btn = tk.Button(master = galeria, image = img12, height = 50, width = 150, command = lambda: asignarIMG('img12'), relief = 'flat')
img12Btn.grid(column = 2, row = 4, padx = 10, pady = 10)

CambiosBtn = tk.Button(master = mainCtn, text = 'Guardar Cambio',command = escribir)
CambiosBtn.pack(padx = 10, pady = 10)
vista.mainloop()