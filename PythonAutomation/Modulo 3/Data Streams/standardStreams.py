#Ejemplo STDIN, STDOUT, STDERR

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
#Cuidado con el ultimo comando que nos dará un error ya que no se puede sumar una cadena de texto