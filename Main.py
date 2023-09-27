import tkinter as tk
from tkinter import ttk 
import subprocess


#Paleta de Colores
BGclr = '#fef6cd'
almClr = '#20c67a'
prfClr = '#3f8880'
admClr = '#9dc09d'
extClr = '#a0fb0e'


# Conteo para bloqueos de secion
BloqueoA = 0
#Inicio de ventana
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

def acceso(tipo, dat1, dat2, dat3):
    datosAlumno = []
    
    if tipo == 'alumno':
        BaseDatos = F'Pantallas/Datos/Alumnos/{dat1}.txt'
        try:
            data = open(BaseDatos)
            alumno = data.read()
            alumno= alumno.split('///\n')
            datosAlumno = alumno[0].split(',')
            BloqueoA = int(datosAlumno[9])

            data.close()
        except:
            print('Sin datos')
            subprocess.run(['python', 'Pantallas/error.py', '404', f'usuario {dat1} no registrado'])
        
        if datosAlumno[6] == dat2 and datosAlumno[8] == dat3:
            if BloqueoA >= 3:
                subprocess.run(['python', 'Pantallas/error.py','X', 'Usuario Bloqueado " Pongase en contacto con el administrador"'])
                return
            print('aceso concedido')
            subprocess.run(['python', 'Pantallas/vistaAlumno.py', datosAlumno[0]])
        else:
            alumnoNew = []
            BloqueoA += 1
            datosAlumno[9] = str(BloqueoA)
            print(datosAlumno)
            datosAlumno = ','.join(datosAlumno)
            print(datosAlumno)
            alumnoNew.append(datosAlumno)
            alumnoNew.append('///\n')  
            alumnoNew.append(alumno[1])
            alumnoNewText = ''.join(alumnoNew)
            try:
                with open(BaseDatos, 'w') as data:
                    data.write(alumnoNewText)
            except:
                print('Error')
            if BloqueoA >= 3:
                subprocess.run(['python', 'Pantallas/error.py','X', 'Usuario Bloqueado " Pongase en contacto con el administrador"'])
            subprocess.run(['python', 'Pantallas/error.py','Datos incorrectos', 'La contraseña o nombre de usuario no coinciden'])

        
    elif tipo == 'profesor':
        BaseDatos = F'Pantallas/Datos/Profesores/{dat1}.txt'
        try:
            data = open(BaseDatos)
            prf = data.read()
            prf= prf.split('///')
            datosProfesor = prf[0].split(',')
            BloqueoP = datosProfesor[5]
            print(prf)
            print(datosProfesor)

            data.close()
        except:
            subprocess.run(['python', 'Pantallas/error.py', '404', f'usuario {dat1} no registrado'])
        
        if datosProfesor[3] == dat2 and datosProfesor[4] == dat3:
            print('aceso concedido')
            subprocess.run(['python', 'Pantallas/vistaProfesor.py', datosProfesor[0]])
        else:
            prfNew = []
            BloqueoP+= 1
            datosProfesor[9] = str(BloqueoA)
            print(datosProfesor)
            datosProfesor = ','.join(datosProfesor)
            print(datosProfesor)
            prfNew.append(datosProfesor)
            prfNew.append('///\n')  
            prfNew.append(prf[1])
            prfNewText = ''.join(prfNew)
            try:
                with open(BaseDatos, 'w') as data:
                    data.write(prfNewText)
            except:
                print('Error')
            if BloqueoP >= 3:
                subprocess.run(['python', 'Pantallas/error.py','X', 'Usuario Bloqueado " Pongase en contacto con el administrador"'])
            subprocess.run(['python', 'Pantallas/error.py','Datos incorrectos', 'La contraseña o nombre de usuario no coinciden'])

    elif tipo == 'admin':
        print('admin')
        with open('Pantallas/Datos/Admin.txt') as data:
            lectura = data.read()
            admin = lectura.split(',')
            print(admin)
            if dat1 == admin[0] and dat2 == admin[1]:
                print('acceso Administrador concedido')
            else:
                subprocess.run(['python', 'Pantallas/error.py','Datos incorrectos', 'La contraseña o nombre de usuario no coinciden'])
                

def getUserData (tipo, paramUno, paramDos, paramTres):
    if tipo == 'alumno':
        carnet = paramUno.get()
        userName = paramDos.get()
        password = paramTres.get()
        print(carnet, userName, password)

        acceso(tipo, carnet, userName, password)

    elif tipo == 'profesor':
        Dpi = paramUno.get()
        userName = paramDos.get()
        password = paramTres.get()
        acceso(tipo, Dpi, userName, password)
    elif tipo == 'admin':
        User = paramUno.get()
        password = paramDos.get()
        acceso(tipo, User, password, password)
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
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, relief = 'flat', command = lambda: getUserData('admin', getUserName, getPassword, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, relief = 'flat', command = lambda: restaurar([LabelB, LabelC, getPassword, getUserName, botones, ingreso, regresar]))
    regresar.grid(column = 4, row = 0, padx = 40)


#Flujo de la aplicacion
Inicio(iniSecion)
iniSecion.title('Academia USAC  iniciar secion')
iniSecion['bg'] = BGclr

iniSecion.mainloop()

