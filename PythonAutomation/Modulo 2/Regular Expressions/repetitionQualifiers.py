import re
#De esta forma nos va a buscar todas las palabras que comiencen por Py y terminen en n, ya que .* indica que busca todas las variaciones posibles
print(re.search(r"Py.*n", "Pygmalion"))#<re.Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r"Py.*n", "Python Programming"))#<re.Match object; span=(0, 17), match='Python Programmin'>

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly-"))
