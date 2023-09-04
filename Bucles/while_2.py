#Todo lo presente aqui no son proyectos, es parte del estudio de Python

def attempts(n):#Declaracion de la funcion attempts con valor n
    x = 1 #Inicializamos la variable x en 1
    while x <= n: #Generamos el bucle while indicando que mientras x sea menor o igual que n
        print("Attempt " + str(x)) #imprima Attempt + el valor que tenga x convertido en string
        x += 1 #Sumamos 1 al valor de x
    print("Done") #Imprimimos realizado

attempts(5) #indicamos que queremos 5 intentos dandole 5 al valor de n