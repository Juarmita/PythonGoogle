#RUN IN LINUX OS
#!/usr/bin/env python3
import sys
import os

filename=sys.argv[1]

if not os.path.exits(filename):#Comprueba si existe el archivo
    with open(filename, 'w') as f:
        f.write("New file created\n")#SI no existe crea el archivo
else:
    print("Error, the file {} already exists!".format(filename))#Si el archivo existe nos manda un mensaje de error
    sys.exit(1)#el mensaje de error es 1