import os
import subprocess

my_env = os.environ.copy()#Lanzamos el metodo de copio del diccionario environ
my_env["PATH"] = os.pathsep.join(["opt/myapp", my_env["PATH"]])#Añadimos un diccionario adicional a la variable de la ruta usando join

result = subprocess.run(["myapp"], env=my_env)#llamamos al comando myapp estableciendo el parametro final env