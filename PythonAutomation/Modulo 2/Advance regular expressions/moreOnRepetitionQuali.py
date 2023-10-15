import re
#En este caso estamos buscando letras que se repitan 5 veces {5}
print(re.search(r"[a-zA-Z]{5}", "a ghost"))#<re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))#<re.Match object; span=(2, 7), match='scary'>
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))#['scary', 'ghost', 'appea']
#Usando \b estamos indicando que queremos palabras completas
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))#['scary', 'ghost']
#Si queremos indicar un rango de palabras usamos \w
print(re.findall(r"\w{5,10}", "I really like strawberries"))#['really', 'strawberri']
#Quitando el limite superior
print(re.findall(r"\w{5,}", "I really like strawberries"))#['really', 'strawberries']
#En este caso añadimos la letra por la que quermos que comience
print(re.search(r"s\w{,20}", "I really like strawberries"))#<re.Match object; span=(14, 26), match='strawberries'>
