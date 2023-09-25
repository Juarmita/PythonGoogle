#Uso del metodo append
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")#Añade al final de la lista el nuevo elemento Kiwi
print(fruits)
#Uso del metodo insert
fruits.insert(0,"Orange")#Con el metodo insert podemos insertar el nuevo elemento en el indice que le indiquemos
print(fruits)
#Uso del metodo remove
fruits.remove("Melon")#Elimina de la lista el primer elemento que coincide con el elemente que le pasamos
print(fruits)
#Uso del metodo pop
fruits.pop(3)#indicamos el indice del elemento que queremos extraer y lo borra de la lista
print(fruits)
#Si indicamos con corchetes un nuevo valor al elemento, lo sobreescribimos
fruits[2] = "Strawberry"#Se sustituye banana por strawberry
print(fruits)