import face_recognition
import cv2
import sys
import os
import pickle

# Cargar el modelo desde el archivo .pkl
carnet = sys.argv[1]

ruta_actual = os.getcwd()
def printer():
    print(validRostro[0])
    video_capture.release()
    cv2.destroyAllWindows()

destino = F"{ruta_actual}\\Pantallas\\Datos\\imagenes\\ImgRegistros\\{carnet}modelo.pkl"

validRostro = [False, False]



with open(destino, "rb") as archivo:
    data = pickle.load(archivo)
    codificaciones = data["codificaciones"]
    etiquetas = data["etiquetas"]

# Inicializar la cámara (puedes ajustar el número de cámara según tus necesidades)
video_capture = cv2.VideoCapture(0)

i = 0

while True:
    ret, frame = video_capture.read()
	
        
    # Encontrar caras en el fotograma
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_location, face_encoding in zip(face_locations, face_encodings):
        # Comparar la cara con el rostro almacenado en el modelo
        matches = face_recognition.compare_faces(codificaciones, face_encoding)

        if True in matches:
            # Si se encuentra una coincidencia, mostrar un recuadro verde
            etiqueta = etiquetas[matches.index(True)]
            color = (0, 255, 0)  # Verde para caras conocidas
            validRostro[0] = True
            i += 1
            
        else:
            etiqueta = -1  # Etiqueta para caras desconocidas
            color = (0, 0, 255)  # Rojo para caras desconocidas

        # Dibujar un rectángulo alrededor de la cara
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

    # Mostrar el resultado en tiempo real
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    if validRostro[0] == True and i == 4:
        break

# Liberar la cámara y cerrar la ventana
printer()

