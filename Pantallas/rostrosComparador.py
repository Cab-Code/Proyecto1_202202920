import face_recognition
import cv2
import pickle

# Cargar el modelo desde el archivo .pkl
with open("modelo_reconocimiento_facial.pkl", "rb") as archivo:
    data = pickle.load(archivo)
    codificaciones = data["codificaciones"]
    etiquetas = data["etiquetas"]

# Inicializar la cámara (puedes ajustar el número de cámara según tus necesidades)
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Encontrar caras en el fotograma
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_location, face_encoding in zip(face_locations, face_encodings):
        # Comparar la cara con las caras almacenadas en el modelo
        matches = face_recognition.compare_faces(codificaciones, face_encoding)

        if True in matches:
            # Si se encuentra una coincidencia, encontrar la etiqueta correspondiente
            first_match_index = matches.index(True)
            etiqueta = etiquetas[first_match_index]
            nombre_persona = f"Persona {etiqueta + 1}"  # Cambiar el formato del nombre según tus etiquetas
            color = (0, 255, 0)  # Verde para caras conocidas
        else:
            etiqueta = -1  # Etiqueta para caras desconocidas
            color = (0, 0, 255)  # Rojo para caras desconocidas
            nombre_persona = "Desconocido"

        # Dibujar un rectángulo alrededor de la cara y mostrar la etiqueta
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, nombre_persona, (left + 6, bottom - 6), font, 0.5, color, 1)

    # Mostrar el resultado en tiempo real
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
video_capture.release()
cv2.destroyAllWindows()