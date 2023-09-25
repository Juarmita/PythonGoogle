name = "Juanma"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
#{:.2f} esto se usa para indicar que solo queremos dos decimales