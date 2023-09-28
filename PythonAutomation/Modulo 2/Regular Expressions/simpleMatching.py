import re
result = re.search(r"aza", "plaza") #la r delanta de "aza" nos indica que es un straing sin procesar(Rawstring)
print(result)#<re.Match object; span=(2, 5), match='aza'>
result = re.search(r"aza", "bazaar")
print(result)#<re.Match object; span=(1, 4), match='aza'>
result = re.search(r"aza", "maze")
print(result)#None

#------Ejemplo 2 ---------#
print(re.search(r"^x", "xenon"))#<re.Match object; span=(0, 1), match='x'>
print(re.search(r"p.ng", "penguin"))#<re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "clapping"))#<re.Match object; span=(4, 8), match='ping'>
print(re.search(r"p.ng", "sponge"))#<re.Match object; span=(1, 5), match='pong'>
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))#Con re.IGNORECASE no hace distincion entre mayusculas y minusculas#<re.Match object; span=(1, 5), match='pong'>
