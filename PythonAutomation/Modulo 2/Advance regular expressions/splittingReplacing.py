import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
#['One sentence', ' Another one', ' And the last one', '']
#Uso de sub
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
#Received an email for [REDACTED]
print(re.sub(r"^([\w .-]*), ([\w .-]*)", r"\2 \1", "Lovelace, Ada"))
#Ada Lovelace