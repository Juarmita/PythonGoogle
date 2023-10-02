import re
print(re.search(r"A.*a", "Argentina"))#<re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"^A.*a$", "Azerbaijan"))#De esa forma e dejamos claro que queremos que empiece y termine con a. #None
print(re.search(r"^A.*a$", "Australia"))#En este caso funciona. #<re.Match object; span=(0, 9), match='Australia'>
#Patrón de validación

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))#<re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
print(re.search(pattern, "this isn't a valid variable"))#None
print(re.search(pattern, "my_variable1"))#<re.Match object; span=(0, 12), match='my_variable1'>. Funciona porque hemos añadido todos los numeros al final en pattern
print(re.search(pattern, "2my_variable1"))#None. No hemos añadido numeros al principio de pattern

