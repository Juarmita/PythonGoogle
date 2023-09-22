x = {}
print(type(x))
#Ejemplo
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)
#Para agregar una nueva entrada en el dictionary
file_counts["cfg"] = 8
print(file_counts)
#Para asignar un nuevo valor a una entrada del diccionario
file_counts["csv"] = 17
print(file_counts)
#Para eliminar una de las entradas usamos del
del file_counts["cfg"]
print(file_counts)