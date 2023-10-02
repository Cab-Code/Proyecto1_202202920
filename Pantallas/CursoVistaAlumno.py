import tkinter as tk
import tkinter.font as tkFont
import subprocess
import sys

argumentosPrograma = sys.argv

nameCurso = str(argumentosPrograma[1])
carnet = str(argumentosPrograma[2])

vista = tk.Tk()
vista.title(F'{nameCurso} {carnet}')
vista.geometry('600x600+20+20')

vista.mainloop()