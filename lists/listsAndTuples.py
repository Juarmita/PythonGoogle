#Tuples es una secuancia de elementos de cualquier tipo que son inmutables
fullname = ('Grace', 'M', 'Hopper')

#Ejemplo en una funcion
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))
print(result)