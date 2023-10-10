import tkinter as tk

# Crear una ventana principal
root = tk.Tk()
root.title("Ejemplo de Frame Desplazable")

# Crear un Frame principal
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

# Crear un Canvas
canvas = tk.Canvas(frame)
canvas.pack(side='left', fill='both', expand=True)

# Agregar una barra de desplazamiento vertical
scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)

# Crear otro Frame dentro del Canvas
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Agregar contenido al Frame interno (inner_frame)
for i in range(50):
    tk.Label(inner_frame, text=f"Elemento {i}").pack()

# Configurar el desplazamiento del Canvas
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_canvas_configure)

# Permitir desplazar el Canvas con la rueda del ratón
def on_canvas_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind("<MouseWheel>", on_canvas_scroll)

# Agregar un botón para demostrar el desplazamiento
tk.Button(inner_frame, text="Botón de Ejemplo").pack()

root.mainloop()