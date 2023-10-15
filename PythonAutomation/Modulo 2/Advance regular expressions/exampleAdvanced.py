#Extracting a PID Using regexes in Python
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])#12345
#Explicacion de \[(\d+)\]: El primer caracter es la barra \ se usa como escape,
# eL [] nos indica que esto es literalmente para fines coincidentes, los () nos indican que tenemos un gurpo de captura
#\d+ esto nos indica que buscamos uno o mas caracteres numericos.

# Vamos a probar con otra cadena que funciona correctamente
result = re.search(regex, "A completeley different string that also has numbers [34567]")
print(result[1])#34567
result = re.search(regex, "99 elephants in a [cage]")
#print(result[1])#TypeError: 'NoneType' object is not subscriptable

#vamos a solucionar el problema anterior

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))#12345
print(extract_pid("99 elephants in a [cage]"))# "SPACE"