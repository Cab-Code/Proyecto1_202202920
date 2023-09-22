alumnos = []

with open('data.txt') as file:
    leer = file.read()

    data = leer.split('\n')
    for elemento in data:
        alumno = elemento.split('-')
        alumnos.append(alumno)
    print(alumnos[1][0]) 

var = '202202915'
i = 0
for alumno in alumnos:
    if alumno[0] != var:
        i = i + 1
    if alumno[0] == var:
        break

print(alumnos[i])

    
