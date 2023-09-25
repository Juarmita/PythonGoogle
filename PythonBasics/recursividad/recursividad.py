def factorial(n): #Declaracion de la funcion factorial
    print("Factorial called with " + str(n))
    if n < 2: #Condicional que define el caso base
        print("Returning 1")
        return 1 #Simplemente devuelve el valor 1
    result = n * factorial(n-1) #Aqui vemos el ejemplo de recursividad 
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)
