import tkinter as tk
from tkinter import ttk 

#PAleta de Colores
BGclr = '#fef6cd'
almClr = '#20c67a'
prfClr = '#3f8880'
admClr = '#9dc09d'
extClr = '#a0fb0e'

def getUserData (paramUno, paramDos, paramTres):
        carnet = paramUno.get()
        userName = paramDos.get()
        password = paramTres.get()

        print(carnet, userName, password)

def borrarWidgets(widgets):
    for widget in widgets:
        widget.pack_forget()


def SecionAlumno (contenedor, admin, alumno, profesor, instruc):
       

    contenedor['bg'] = almClr
    borrarWidgets([admin, alumno, profesor])
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = almClr


    LabelA = tk.Label(master = contenedor, text = 'Carnet', bg = almClr)
    getCarnet = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg ='#20c67c')
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = almClr,)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')
    getPassword.config(show="*")

    LabelA.pack(pady = 5)
    getCarnet.pack(pady = 10)
    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = almClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, relief = 'flat', command = lambda: getUserData(getCarnet, getUserName, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    registro = tk.Button(master = botones, text = 'registrarse', bg = extClr, relief = 'flat')
    registro.grid(column = 2, row = 0, padx = 40)



def Inicio (iniSecion):
    
    alto = iniSecion.winfo_reqheight()
    largo = iniSecion.winfo_reqwidth()

    contenedor = tk.Frame(iniSecion,padx = 50, pady = 60, width = 600, height = 400)
    contenedor['bg'] = BGclr
    instruccion = tk.Label(master = contenedor, text = 'Iniciar secion como...')
    instruccion.pack(pady = 20)
    instruccion['bg'] = BGclr


    btnAlumno = tk.Button(master = contenedor, text = 'Alumno', width = 100, relief = 'flat', bg = almClr, command = lambda:SecionAlumno(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion))
    btnProfesor= tk.Button(master = contenedor, text = 'Profesor', width = 100, relief = 'flat', bg = prfClr)
    btnAdmin = tk.Button(master = contenedor, text = 'Administrador', width = 100, relief = 'flat', bg = admClr)

    contenedor.pack(pady = alto/2 - 20, padx = 100) 
    btnAdmin.pack(pady = 10)
    btnProfesor.pack(pady = 10)
    btnAlumno.pack(pady = 10)
    iniSecion.update()
    
#Inicio de ventana 
#Flujo de la aplicacion
iniSecion = tk.Tk()
Inicio(iniSecion)
iniSecion.title('Academia USAC  iniciar secion')
iniSecion['bg'] = BGclr

iniSecion.mainloop()

