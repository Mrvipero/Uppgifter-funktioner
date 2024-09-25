import math

x1 = float(input("skriv in första x: "))
x2 = float(input("skriv in andra x: "))
y1 = float(input("skriv in första y: "))
y2 = float(input("skriv in andra y: "))

avstånd = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"Avståndet mellan x kordinaterna {x1}, {x2} och y kordinaterna {y1}, {y2} är {avstånd}")
