with open("prueba.txt") as file:
    for line in file:
        print(line.upper())

with open("prueba.txt") as file:
    for line in line:
        print(line.strip().upper())