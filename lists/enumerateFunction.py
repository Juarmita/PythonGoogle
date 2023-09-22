#Uso de la funcion enumerate
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):#La funcion enumerate devuelve los elementos del array odenados en lista
    #index hace referencia al indice del elemento en la secuencia
    #person es el elemento en el array
    print("{} - {}".format(index + 1, person))