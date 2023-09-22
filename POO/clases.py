class Apple: #Creamos una nueva clase
    pass #Con pass indicamos que está vacio

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())
golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"