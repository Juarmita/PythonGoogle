import re

result = re.search(r"^(\w*), (\w*)$", "Lovlace, Ada")
print(result)#<re.Match object; span=(0, 12), match='Lovlace, Ada'>
#\w coincidira con letras, numeros y guiones bajos
