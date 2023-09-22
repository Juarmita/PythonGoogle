file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:#Usando simplemente el bucle for nos devuelve el texto de la entrada
    print(extension)
#Para acceder a la dupla de texto y datos
for ext, amount in file_counts.items():#obtenemos el par de elemento y valor
    print("There are {} files with the .{} entension".format(amount, ext))

print(file_counts.keys())#Obtenemos solo las claves
print(file_counts.values())#obtenemos solo los valores
#Para iterar solo sobre los valores
for value in file_counts.values():
    print(value)

#Ejemplo. Aqui comprobamos cuantas veces aparece una letra

def count_letters(text):#Declaramos la funcion count_letters
    result = {} #creamos un nuevo diccionario vacio
    for letter in text: #iteracion buscando la letra (letter) en text
        if letter not in result: #si la letra no está en resultado
            result[letter] = 0 # a resultado no le sumamos nada
        result[letter] += 1 #si la letra se encuentra suma 1
    return result #nos devuelve el valor de result
print(count_letters("aaaaa"))
print(count_letters("Maria Fernanda"))