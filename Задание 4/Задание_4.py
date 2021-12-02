x = int(input("Введите х: "))
q = int(input("Введите q: "))
x2 = x * x
cos = 1
a = 1
b = -1
c = 2
d = 2

while ((x2 / c ) >= q ):
    cos = cos + b * x2 / c
    a = a + 1
    d = d + 2
    x2 = x2 * x * x
    c = c * (d - 1) * d
    b = b * (-1)
    print("cos(x): "+str(cos))

