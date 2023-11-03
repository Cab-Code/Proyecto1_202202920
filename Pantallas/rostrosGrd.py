import sys
import shutil
import os
import subprocess

carnet =sys.argv[1]


subprocess.run(['python', 'Pantallas/rostrosModelo.py', carnet])
