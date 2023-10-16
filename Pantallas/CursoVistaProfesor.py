import tkinter as tk
import tkinter.font as tkFont
import subprocess
from PIL import ImageTk, Image
import sys

argumentosPrograma = sys.argv

vista = tk.Tk()
tituloFont = tkFont.Font(family = "Lucida Grande", size = 20)
textoFont = tkFont.Font(family = "Lucida Grande", size = 12)
nameCurso = str(argumentosPrograma[1])
carnet = str(argumentosPrograma[2])


curso = []

ALumnosData = []
vista.title(F'{nameCurso} {carnet}')
vista.geometry('600x600+20+20')



def editarCurso():
    print('Posibilidad de editar curso...')
    subprocess.run(['python', 'Pantallas/editarcursoPrf.py',nameCurso])




with open(F'Pantallas/Datos/Cursos/{nameCurso}.txt') as BaseDatos:
    lectura = BaseDatos.read()
    curso = lectura.split('///\n')
    ALumnosData = curso[4]
    ALumnosData = ALumnosData.split('\n')

titulo = curso[0]
descripcion = curso[1]
imgCurso = curso[3]
profesor = curso[2]

bannerImg = ImageTk.PhotoImage(Image.open(F'Pantallas/Datos/Imagenes/{imgCurso}.jpg'))
banner = tk.Label(master = vista, image = bannerImg, height = 150)
banner.pack()



frame = tk.Frame(vista)
frame.pack(fill='both', expand=True)
canvas = tk.Canvas(frame)
canvas.pack(side='left', fill='both', expand=True)
scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_canvas_configure)

def on_canvas_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind("<MouseWheel>", on_canvas_scroll)


main = tk.Frame(vista, width  = 100,padx = 110)
main.pack()

tituloVs = tk.Label(master = main, font = tituloFont, text = titulo)
descripcionVs = tk.Label(master = main, font = textoFont, text = descripcion, width = 40)

tituloVs.pack(pady = 20)
descripcionVs.pack()
prfDatos = []
with open(F'Pantallas/Datos/Profesores/{profesor}.txt') as profesorDB:
    leer = profesorDB.read()
    prfDatos = leer.split(',')

prfesor = tk.Label(master = main, text = F'Catedratico: {prfDatos[1]} {prfDatos[2]}')
prfesor.pack(pady = 10)



alumnosDataCtn = tk.Frame(main)
alumnosDataCtn.pack()

for alumno in ALumnosData:
    alumno = alumno.split(':')
    alumnoCtn = tk.Frame(alumnosDataCtn, padx = 30, pady = 10, relief = 'solid', borderwidth = 1)
    alumnoCtn.pack(pady = 5, padx = 10)
    textoCarnet = tk.Label(alumnoCtn, text = F'{alumno[0]}: {alumno[1]}', font = tituloFont)
    textoCarnet.pack()
    



editar = tk.Button(main, text = 'Editar Curso', command = editarCurso)
editar.pack(pady = 50)

editar = tk.Button(main, text = 'Editar Notas', command = editarCurso)
editar.pack(pady = 50)

canvas.create_window((0, 0), window= main, anchor='nw')







vista.mainloop()