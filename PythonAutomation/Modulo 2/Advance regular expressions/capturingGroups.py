import re

result = re.search(r"^(\w*), (\w*)$", "Lovlace, Ada")
print(result)#<re.Match object; span=(0, 12), match='Lovlace, Ada'>
#\w coincidira con letras, numeros y guiones bajos
print(result.groups())#El metodo groups nos devuelve una dupla de dos elementos
print(result[0])#Lovlace, Ada. Nos devuelve el grupo entero
print(result[1])#Lovlace. Devuelve el primer valor del grupo.
print(result[2])#Ada. Nos devuelve el segundo valor del grupo
#Podemos generar los nombres usando estos indices
print("{} {}".format(result[2], result[1]))#Ada Lovlace

#vamos a crear una funcion que haga esto por nosotros
def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
