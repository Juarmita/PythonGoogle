#Iteracion sobre listas y tuplas
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]#Lista sobre la que vamos a iterar
chars = 0
for animal in animals:#Para cada uno de los strings obtenemos su longitud
    chars += len(animal)#Aqui obtenemos la longitud del string de CADA ANIMAL

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))#Aqui sacamos el total de letras y el promedio
#En el segundo len obtenemos la longitud del ARRAY