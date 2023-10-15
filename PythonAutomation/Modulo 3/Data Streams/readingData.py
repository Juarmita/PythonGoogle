#!/usr/bin/env python3

name = input("Please enter your name: ")
print("Hello, " + name)

#Please enter your name: Juanma
#Hello, Juanma

#Second example

def to_seconds(hours, minutes, seconds): #Definimos una funcion que convierta en segundos las horas, minutso y segundos
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")#Imprime un mensaje de bienvenida antes de entrar al bucle

cont = "y"#Inicializamos la variable cont para comprobar si el usuario quiere continuar
while(cont.lower() == "y"): #Dentro del bucle pedimos al usuario que introduzca el numero de horas, minutos y segundos que quiere convertir
    hours = int(input("Enter the number or hours: "))
    minutes = int(input ("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))#Aqui llamamos a la funcion e imprimimos el resultado
    print()
    cont = input("Do you want to do anoter conversion? [y to continue] ")

print("Good bye!")
