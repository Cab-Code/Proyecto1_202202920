import tkinter as tk
import subprocess

colorDos = '#9dc09d'
colorUno = '#9dc09d'

datos = ['202202920', 'Estuardo', 'Cabrera', '3050227170117', '12/04/2004', '56232849', 'EstCab', 'correo@gmail.com','contra', 'Bloqueado']

carnet = datos[0]
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

def inicio():
    inicio = tk.Frame(master = vista, bg = '#9dc09d')
    datos = tk.Label(text = F"carnet: {carnet}     DPI:{Dpi} \n {nombre} {apelli}       {fecha} \n {username}        {correo}")
    inicio.pack(pady = 10)
    datos.pack(padx = 10)

inicio()
vista.mainloop()