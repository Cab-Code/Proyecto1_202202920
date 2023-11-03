import face_recognition
import sys
import os
import pickle

carnet = sys.argv[1]

ruta_actual = os.getcwd()


destino = F"{ruta_actual}\\Pantallas\\Datos\\imagenes\\ImgRegistros\\{carnet}"
ruta_imagenes_persona = destino  # Cambia la ruta según tu estructura de carpetas

# Inicializar listas para almacenar las codificaciones y etiquetas
codificaciones = []
etiquetas = []

# Enumerar las imágenes en el directorio ruta_imagenes_persona
for nombre_imagen in os.listdir(ruta_imagenes_persona):
    # Cargar la imagen de la persona
    ruta_imagen = os.path.join(ruta_imagenes_persona, nombre_imagen)
    imagen = face_recognition.load_image_file(ruta_imagen)
    codificacion_rostro = face_recognition.face_encodings(imagen)

    if codificacion_rostro:
        # Si se detecta al menos un rostro, se agrega la codificación y etiqueta
        codificaciones.append(codificacion_rostro[0])
        etiquetas.append(0)  # Usamos la etiqueta 0 para esta única persona

# Crear un diccionario con las codificaciones y etiquetas
datos = {"codificaciones": codificaciones, "etiquetas": etiquetas}

# Guardar el modelo en un archivo .pkl
with open(F"modelo-{carnet}.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

print("Modelo de reconocimiento facial creado y guardado en modelo_persona.pkl")