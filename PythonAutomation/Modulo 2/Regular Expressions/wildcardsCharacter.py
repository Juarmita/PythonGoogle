import re
print(re.search(r"[Pp]ython", "Python"))#<re.Match object; span=(0, 6), match='Python'>
print(re.search(r"[a-z]way", "The end of the highway"))#<re.Match object; span=(18, 22), match='hway'>
print(re.search(r"[a-z]way", "What a way to go"))#None
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))#<re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))#<re.Match object; span=(4, 5), match=' '. Con ^ indicamos que buscamos cualquier parametro que no sea una letra
print(re.search(r"cat|dog", "I like cats."))#<re.Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I like dogs."))#<re.Match object; span=(7, 10), match='dog'>
print(re.search(r"cat|dog", "I like both dogs and cats."))#<re.Match object; span=(12, 15), match='dog'>. En este caso solo nos devuelve la primera coincidencia

#-----Para encontrar todas las coincidencias usamos la funcion findall
print(re.findall(r"cat|dog", "I like both dog and cats"))#['dog', 'cat']


