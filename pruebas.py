with open('data.txt') as file:
    leer = file.read()

    data = leer.split('\n')
    alumnos = []
    for elemento in data:
        alumno = elemento.split('-')
        alumnos.append(alumno)
    print(alumnos[1][0]) 

    