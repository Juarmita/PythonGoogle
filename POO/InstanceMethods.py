class Piglet: #Creamos la clase
    pass



#--------------------#
class Piglet:
    def speak(self):
        print("oink oink")

hamlet = Piglet()
print(hamlet.speak())

#---------#
class Piglet2:
    name = "piglet"
    def speak(self):
        print("Oink! i'm {}! Oink!".format(self.name))#estamos accediendo al nombre en la clase Pglet2

hamlet = Piglet2()
hamlet.name = "Hamlet"
hamlet.speak()
petunia = Piglet2()
petunia.name = "Petunia"
petunia.speak()

#Ejemplo en el que nos devuelve un valor#
class PigletValue:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = PigletValue()
print(piggy.pig_years())
piggy.years = 2
print(piggy.pig_years())