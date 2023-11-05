import face_recognition
import cv2
import sys
import os
import pickle


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


video_capture = cv2.VideoCapture(0)

i = 0

while True:
    ret, frame = video_capture.read()
	

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_location, face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(codificaciones, face_encoding)

        if True in matches:

            etiqueta = etiquetas[matches.index(True)]
            color = (0, 255, 0)
            validRostro[0] = True
            i += 1
            
        else:
            etiqueta = -1 
            color = (0, 0, 255) 

      
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)


    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    if validRostro[0] == True and i == 4:
        break


printer()

