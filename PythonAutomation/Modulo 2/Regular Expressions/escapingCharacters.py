#Detección de caracteres especiales.
import re
print(re.search(r"\.com", "welcome"))#None. Con \. conseguimos que se busque el . en el trozo que queremos
print(re.search(r"\.com", "mydomain.com"))#<re.Match object; span=(8, 12), match='.com'>
print(re.search(r"\w*", "This is an example"))#<re.Match object; span=(0, 4), match='This'>  
print(re.search(r"\w*", "And_this_is_another"))#<re.Match object; span=(0, 19), match='And_this_is_another'>
