import re #importamos re que es usado para la busqueda de texto
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade" #Este es el texto de ejemplo
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
