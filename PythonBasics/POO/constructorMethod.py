class Apple:
    def __init__(self, color, flavor):#El constructor siempre se llama __init__
        self.color = color
        self.flavor = flavor
    def __str__(self): #Con el metodo especial __str__ le decimos a python que queremos que nos imprima por pantalla el string
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
jonafgold = Apple("red", "sweet")
print(jonafgold)
