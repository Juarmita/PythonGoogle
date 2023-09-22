multiples = []#Asingamos un array vacio a multiples
for x in range(1, 11): #Creamos un bucle que va en un rango de 1 al 11
    multiples.append(x*7)#Agregamos a la lista multiples en cada iteracion el valor del rango multiplicado por 7

    print(multiples)

#Forma más rapida de hacer lo anterior
multiples = [x*7 for x in range(1,11)]
print(multiples)

#Otro ejemplo
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

#Otro
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)