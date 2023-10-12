import tkinter as tk
import tkinter.font as tkFont
import subprocess



vista = tk.Tk()
vista.title('Administrador')
vista.geometry('1000x655+0+0')
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
texto = tk.Label(vista, text = 'Administrador', font = tituloFont)
texto.pack()
mainCtn = tk.Frame(vista)
mainCtn.pack()



def asignarMaestro():
    subprocess.run(['python', 'Pantallas/asigProfesor.py'])
def desbloquear():
    subprocess.run(['python', 'Pantallas/error.py', 'codigo', 'Desbloquear'])
def crearCurso():
    subprocess.run(['python', 'Pantallas/error.py', 'codigo', 'Craer curso'])



asignarMaestroCtn = tk.Frame(mainCtn)
asignarMaestroCtn.grid(column = 1, row = 1, padx = 50, pady = 200)
maestroBtn = tk.Button(asignarMaestroCtn, font = tituloFont, text = 'Inscribir Catedratico', command = asignarMaestro)
maestroBtn.pack(pady = 50)

DesbloquearCtn = tk.Frame(mainCtn)
DesbloquearCtn.grid(column = 2, row = 1, pady = 200)
DesqBtn = tk.Button(DesbloquearCtn, font = tituloFont, text = 'Desbloquear Usuario', command = desbloquear)
DesqBtn.pack(pady = 50)

CursoCtn = tk.Frame(mainCtn)
CursoCtn.grid(column = 3, row = 1, padx = 50, pady = 200)
CursoBtn = tk.Button(CursoCtn, font = tituloFont, text = 'Crear Curso', command = crearCurso)
CursoBtn.pack(pady = 50)





vista.mainloop()