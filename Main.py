import tkinter as tk
import tkinter.font as tkFont
import subprocess
import bcrypt



salt = b'$2b$12$ASCDyiUrL20F696Dwg8Iw.'

#Paleta de Colores
BGclr = '#fef6cd'
almClr = '#20c67a'
prfClr = '#3f8880'
admClr = '#9dc09d'
extClr = '#a0fb0e'

accesoRostroScan = [False]


# Conteo para bloqueos de secion
BloqueoA = 0
#Inicio de ventana
iniSecion = tk.Tk()
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
iniSecion.geometry('900x650+0+0')
contenedor = tk.Frame(iniSecion,padx = 50, pady = 40, width = 600, height = 400)
instruccion = tk.Label(master = contenedor, text = 'Iniciar secion como...', font = tituloFont)
btnAlumno = tk.Button(master = contenedor, text = 'Alumno', width = 100, relief = 'flat', bg = almClr, command = lambda:SecionAlumno(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion), font = textoFont)
btnProfesor= tk.Button(master = contenedor, text = 'Profesor', width = 100, relief = 'flat', bg = prfClr,  command = lambda:SecionProfesor(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion), font = textoFont)
btnAdmin = tk.Button(master = contenedor, text = 'Administrador', width = 100, relief = 'flat', bg = admClr, command = lambda:SecionAdmin(contenedor, btnAdmin, btnAlumno, btnProfesor, instruccion), font = textoFont)

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


def scannearRostro():
    subprocess.run(['python', 'Pantallas/rostrosComparador.py'])

def acceso(tipo, dat1, dat2, dat3):
    if accesoRostroScan[0] == False:
            subprocess.run(['python', 'Pantallas/error.py', 'Ingrese sus datos', f'Debe realizar el analizis de rostro'])

    datosAlumno = []
    print(dat1)
    BloqueoA = 0
    
    if tipo == 'alumno':
        BaseDatos = F'Pantallas/Datos/Alumnos/{dat1}.txt'
        try:
            data = open(BaseDatos)
            alumno = data.read()
            alumno= alumno.split('///\n')
            datosAlumno = alumno[0].split(',')
            BloqueoA = int(datosAlumno[9])
            carnet = datosAlumno[0]
            data.close()
        except:
            subprocess.run(['python', 'Pantallas/error.py', '404', f'usuario {dat1} no registrado'])

        contraseña = datosAlumno[8]
        contraseña = bytes(contraseña, 'utf-8')
        contraseñaGet = bytes(dat3,'utf-8')

            
        if datosAlumno[6] == dat2 and bcrypt.checkpw(contraseñaGet,contraseña):
            if BloqueoA >= 3:
                subprocess.run(['python', 'Pantallas/error.py','X', 'Usuario Bloqueado " Pongase en contacto con el administrador"'])
                return
            BloqueoA = 0
            alumnoNew = []
            datosAlumno[9] = str(BloqueoA)
            datosAlumno = ','.join(datosAlumno)
            alumnoNew.append(datosAlumno)
            alumnoNew.append('///\n')  
            alumnoNew.append(alumno[1])
            alumnoNewText = ''.join(alumnoNew)
            try:
                with open(BaseDatos, 'w') as data:
                    data.write(alumnoNewText)
            except:
                subprocess.run(['python', 'Pantallas/error.py','System Error', 'Ha ocorrido un error'])
            #iniSecion.destroy()
            subprocess.run(['python', 'Pantallas/vistaAlumno.py', carnet])

        else:
            alumnoNew = []
            BloqueoA += 1
            datosAlumno[9] = str(BloqueoA)
            datosAlumno = ','.join(datosAlumno)
            alumnoNew.append(datosAlumno)
            alumnoNew.append('///\n')  
            alumnoNew.append(alumno[1])
            alumnoNewText = ''.join(alumnoNew)
            try:
                with open(BaseDatos, 'w') as data:
                    data.write(alumnoNewText)
            except:
                subprocess.run(['python', 'Pantallas/error.py','System Error', 'Ha ocurrido un error'])
            if BloqueoA >= 3:
                subprocess.run(['python', 'Pantallas/error.py','X', 'Usuario Bloqueado " Pongase en contacto con el administrador"'])
            subprocess.run(['python', 'Pantallas/error.py','Datos incorrectos', 'La contraseña o nombre de usuario no coinciden'])

        
    elif tipo == 'profesor':
        BaseDatosPr = F'Pantallas/Datos/Profesores/{dat1}.txt'
        try:
            data = open(BaseDatosPr)
            prf = data.read()
            prf= prf.split('///')
            datosProfesor = prf[0].split(',')
            BloqueoP = datosProfesor[7]
            data.close()
        except:
            subprocess.run(['python', 'Pantallas/error.py', '404', f'usuario {dat1} no registrado'])
        contraseña = datosProfesor[6]
        contraseña = bytes(contraseña, 'utf-8')
        contraseñaGet = bytes(dat3,'utf-8')
        if datosProfesor[5] == dat2 and bcrypt.checkpw(contraseñaGet,contraseña):
            subprocess.run(['python', 'Pantallas/vistaProfesor.py', datosProfesor[0]])
        else:
            prfNew = []
            BloqueoP = int(BloqueoP)
            BloqueoP+= 1
            datosProfesor[7] = str(BloqueoP)
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
            contraseña = admin[1]
            contraseña = bytes(contraseña, 'utf-8')
            contraseñaGet = bytes(dat3,'utf-8')

            if dat1 == admin[0] and  bcrypt.checkpw(contraseñaGet,contraseña):
                subprocess.run(['python', 'Pantallas/vistaAdmin.py'])
            else:
                subprocess.run(['python', 'Pantallas/error.py','Datos incorrectos', 'La contraseña o nombre de usuario no coinciden'])
                

def getUserData (tipo, paramUno, paramDos, paramTres):
    if tipo == 'alumno':
        carnet = paramUno.get()
        userName = paramDos.get()
        password = paramTres.get()
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

def asignarAlumno():
    subprocess.run(['python', 'Pantallas/AsignarAlumno.py'])

def SecionAlumno (contenedor, admin, alumno, profesor, instruc):
       
    borrarWidgets([admin, alumno, profesor])
    contenedor['bg'] = almClr
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = almClr

    
    scannerR = tk.Button(master =  contenedor, text = 'Escaneear Rostro', bg = extClr, relief = 'flat', command = scannearRostro)

    LabelA = tk.Label(master = contenedor, text = 'Carnet', bg = almClr, font = textoFont)
    getCarnet = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)

    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg ='#20c67c', font = textoFont)
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = almClr, font = textoFont)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)
    getPassword['show'] = '*'

    LabelA.pack(pady = 5)
    getCarnet.pack(pady = 10)
    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)
    scannerR.pack()

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = almClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, relief = 'flat', command = lambda: getUserData('alumno',getCarnet, getUserName, getPassword), font = textoFont)
    ingreso.grid(column = 0, row = 0, padx = 20)
    registro = tk.Button(master = botones, text = 'Nuevo Usuario', bg = extClr, relief = 'flat', font = textoFont, command = asignarAlumno)
    registro.grid(column = 2, row = 0, padx = 20)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, relief = 'flat', command = lambda: restaurar([LabelA, LabelB, LabelC, getCarnet, getPassword, getUserName, botones, ingreso, registro, regresar]), font = textoFont)
    regresar.grid(column = 4, row = 0, padx = 20)

def SecionProfesor (contenedor, admin, alumno, profesor, instruc):
       
    borrarWidgets([admin, alumno, profesor])
    contenedor['bg'] = prfClr
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = prfClr

    

    LabelA = tk.Label(master = contenedor, text = 'DPI', bg = prfClr, font = textoFont)
    getDPI = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)

    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg = prfClr, font = textoFont)
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = prfClr, font = textoFont)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)
    getPassword['show'] = '*'

    LabelA.pack(pady = 5)
    getDPI.pack(pady = 10)
    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = prfClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, font = textoFont, relief = 'flat', command = lambda: getUserData('profesor',getDPI, getUserName, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, font = textoFont, relief = 'flat', command = lambda: restaurar([LabelA, LabelB, LabelC, getDPI, getPassword, getUserName, botones, ingreso, regresar]))
    regresar.grid(column = 4, row = 0, padx = 40)

def SecionAdmin (contenedor, admin, alumno, profesor, instruc):
       
    borrarWidgets([admin, alumno, profesor])
    contenedor['bg'] = admClr
    instruc['text'] = 'Ingrese sus datos'
    instruc['bg'] = admClr

    
    LabelB = tk.Label(master = contenedor, text = 'Nombre de Usuario', bg = admClr, font = textoFont)
    getUserName = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)

    LabelC = tk.Label(master = contenedor, text = 'Contraseña', bg = admClr, font = textoFont)
    getPassword = tk.Entry(master = contenedor, width = 100, bg = BGclr, relief = 'flat', font = textoFont)
    getPassword['show'] = '*'

    LabelB.pack(pady = 5)
    getUserName.pack(pady = 5)
    LabelC.pack(pady = 5)
    getPassword.pack(pady = 10)

    botones = tk.Frame(contenedor ,padx = 50, pady = 20, bg = admClr)
    botones.pack()
    ingreso = tk.Button(master = botones, text = 'Ingresar', bg = extClr, font = textoFont, relief = 'flat', command = lambda: getUserData('admin', getUserName, getPassword, getPassword))
    ingreso.grid(column = 0, row = 0, padx = 40)
    regresar = tk.Button(master = botones, text = 'regresar', bg = extClr, font = textoFont, relief = 'flat', command = lambda: restaurar([LabelB, LabelC, getPassword, getUserName, botones, ingreso, regresar]))
    regresar.grid(column = 4, row = 0, padx = 40)


#Flujo de la aplicacion
Inicio(iniSecion)
iniSecion.title('Academia USAC  iniciar secion')
iniSecion['bg'] = BGclr

iniSecion.mainloop()

