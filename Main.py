import tkinter as tk
from tkinter import ttk 

#Paleta de Colores
BGclr = '#fef6cd'
almClr = '#20c67a'
prfClr = '#3f8880'
admClr = '#9dc09d'
extClr = '#a0fb0e'

#Inicio de ventana
# 
 
iniSecion = tk.Tk()
iniSecion.geometry('800x600+0+0')
contenedor = tk.Frame(iniSecion,padx = 50, pady = 60, width = 600, height = 400)
instruccion = tk.Label(master = contenedor, text = 'Iniciar secion como...')
btnAlumno = tk.Button(master = contenedor, text = 'Alumno', width = 100, relief = 'flat', bg = almClr, command = lambda:SecionAlumno(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion))
btnProfesor= tk.Button(master = contenedor, text = 'Profesor', width = 100, relief = 'flat', bg = prfClr,  command = lambda:SecionProfesor(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion))
btnAdmin = tk.Button(master = contenedor, text = 'Administrador', width = 100, relief = 'flat', bg = admClr, command = lambda:SecionAdmin(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion))

def Inicio (iniSecion):
    
    alto = iniSecion.winfo_reqheight()
    largo = iniSecion.winfo_reqwidth()

    
    contenedor['bg'] = BGclr
    instruccion.pack(pady = 20)
    instruccion['bg'] = BGclr


   
    contenedor.pack(pady = alto/2 - 20, padx = 100) 
    btnAdmin.pack(pady = 10)
    btnProfesor.pack(pady = 10)
    btnAlumno.pack(pady = 10)
    iniSecion.update()

def acceso(data, dat1, dat2, dat3):
    usuarios = []
    sesion = []
    # Obtener los datos
    with open(f'{data}') as BD:
        lectura = BD.read()

        Datos = lectura.split('\n')
        for elemento in Datos:
            
            usuario = elemento.split('-')
            usuarios.append(usuario)
    #busqueda de usuario y compara
    #comparacion de valores
    i = 0
    for usuario in usuarios:
        if usuario[0] != dat1:
            i+=1
        elif usuario[0] == dat1:
            break
        
    print(i, len(usuarios))
    if i < len(usuarios):
        sesion = usuarios[i]
        if sesion[2] == dat2 and sesion[3] == dat3:
            print('Accesando a la pagina')
        else:
            print('Acceso Denegado: Los datos que esta ingresando no son los asociados al DPI o Carnet')
    else:
        print('El Carnet o DPI no esta registrado')

    print(sesion)



def getUserData (tipo, paramUno, paramDos, paramTres):
    if tipo == 'alumno':
        carnet = paramUno.get()
        userName = paramDos.get()
        password = paramTres.get()
        print(carnet, userName, password)

        acceso('data.txt', carnet, userName, password)

    elif tipo == 'profesor':
        Dpi = paramUno.get()
        userName = paramDos.get()
        password = paramTres.get()
        print(Dpi, userName, password)
        print('Profesor')
    elif tipo == 'Admin':
        print('Administrador')


        

def borrarWidgets(widgets):
    for widget in widgets:
        widget.pack_forget()

def restaurar(widgets):
    borrarWidgets(widgets)

    contenedor['bg'] = BGclr
    instruccion['bg'] = BGclr
    instruccion['text'] = 'Iniciar secion como...'
    btnAdmin.pack(pady = 10)
    btnProfesor.pack(pady = 10)
    btnAlumno.pack(pady = 10)



def SecionAlumno (contenedor, admin, alumno, profesor, instruc):
       
    borrarWidgets([admin, alumno, profesor])
    contenedor['bg'] = almClr
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = almClr

    

    LabelA = tk.Label(master = contenedor, text = 'Carnet', bg = almClr)
    getCarnet = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg ='#20c67c')
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = almClr,)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')
    getPassword['show'] = '*'

    LabelA.pack(pady = 5)
    getCarnet.pack(pady = 10)
    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = almClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, relief = 'flat', command = lambda: getUserData('alumno',getCarnet, getUserName, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    registro = tk.Button(master = botones, text = 'Nuevo Usuario', bg = extClr, relief = 'flat')
    registro.grid(column = 2, row = 0, padx = 40)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, relief = 'flat', command = lambda: restaurar([LabelA, LabelB, LabelC, getCarnet, getPassword, getUserName, botones, ingreso, registro, regresar]))
    regresar.grid(column = 4, row = 0, padx = 40)

def SecionProfesor (contenedor, admin, alumno, profesor, instruc):
       
    borrarWidgets([admin, alumno, profesor])
    contenedor['bg'] = prfClr
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = prfClr

    

    LabelA = tk.Label(master = contenedor, text = 'DPI', bg = prfClr)
    getDPI = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg = prfClr)
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = prfClr,)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')
    getPassword['show'] = '*'

    LabelA.pack(pady = 5)
    getDPI.pack(pady = 10)
    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = prfClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, relief = 'flat', command = lambda: getUserData('profesor',getDPI, getUserName, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, relief = 'flat', command = lambda: restaurar([LabelA, LabelB, LabelC, getDPI, getPassword, getUserName, botones, ingreso, regresar]))
    regresar.grid(column = 4, row = 0, padx = 40)

def SecionAdmin (contenedor, admin, alumno, profesor, instruc):
       
    borrarWidgets([admin, alumno, profesor])
    contenedor['bg'] = admClr
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = admClr

    
    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg = admClr)
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = admClr,)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat')
    getPassword['show'] = '*'

    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = admClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, relief = 'flat', command = lambda: getUserData('admin', getUserName, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, relief = 'flat', command = lambda: restaurar([LabelB, LabelC, getPassword, getUserName, botones, ingreso, regresar]))
    regresar.grid(column = 4, row = 0, padx = 40)


#Flujo de la aplicacion
Inicio(iniSecion)
iniSecion.title('Academia USAC  iniciar secion')
iniSecion['bg'] = BGclr

iniSecion.mainloop()

