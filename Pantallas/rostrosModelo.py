import face_recognition
import sys
import os
import pickle
import shutil

carnet = sys.argv[1]

ruta_actual = os.getcwd()


destino = F"{ruta_actual}\\Pantallas\\Datos\\imagenes\\ImgRegistros"
ruta_imagenes_persona = destino + '\\temp'  
codificaciones = []
etiquetas = []

for nombre_imagen in os.listdir(ruta_imagenes_persona):
    # Cargar la imagen de la persona
    ruta_imagen = os.path.join(ruta_imagenes_persona, nombre_imagen)
    imagen = face_recognition.load_image_file(ruta_imagen)
    codificacion_rostro = face_recognition.face_encodings(imagen)

    if codificacion_rostro:
        codificaciones.append(codificacion_rostro[0])
        etiquetas.append(0)  

datos = {"codificaciones": codificaciones, "etiquetas": etiquetas}

with open(F"{destino}\\{carnet}modelo.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

print("Modelo de reconocimiento facial creado y guardado en modelo_persona.pkl")

shutil.rmtree(ruta_imagenes_persona)