import sys
import shutil
import os
import subprocess

carnet =sys.argv[1]
ruta_actual = os.getcwd()

origen = F"{ruta_actual}\\Pantallas\\Datos\\imagenes\\ImgRegistros\\temp"
destino = F"{ruta_actual}\\Pantallas\\Datos\\imagenes\\ImgRegistros\\{carnet}"



try:
    shutil.rmtree(destino)
    print(f"La carpeta '{destino}' ha sido eliminada.")
except OSError as error:
    print(f"No se pudo eliminar la carpeta: ERRRRRRROOOOOORRRRR")



print(origen, destino)

shutil.copytree(origen, destino)
shutil.rmtree(origen)

subprocess.run(['python', 'Pantallas/rostrosModelo.py'])
