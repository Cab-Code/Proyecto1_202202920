import tkinter as tk
import subprocess
import sys
argumentos = sys.argv
print(len(argumentos))
print(argumentos[len(argumentos) - 1])
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
    inicio = tk.Frame(master = vista)
    inicio['bg'] = '#9dc09d'
    datos = tk.Label(master = inicio, text = F"carnet: {carnet}     DPI:{Dpi} \n\n {nombre} {apelli}       {fecha} \n\nusuario: {username}        {correo}")
    datos['bg'] = '#9dc09d'
    inicio.pack(pady = 10)
    datos.pack(padx = 10)

inicio()
vista.mainloop()