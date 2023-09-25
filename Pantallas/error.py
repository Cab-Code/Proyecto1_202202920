import tkinter as tk
import sys

argumentos = sys.argv

codigo = argumentos[1]
errores = argumentos[2]


error = tk.Tk()
error.geometry('300x100')
error.title(codigo)

errorText = tk.Label(master = error, text = errores)
errorText.pack(pady = 40)

error.mainloop()