import math

print("Введите коэффициенты для уравнения ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    x = - c / b
    print("x = " + str(x))

if b == 0:
    x = math.sqrt(- c / a)
    print("x = " + str(x))

elif a > 0:
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = " + str(discr))

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = " + str(x1), "\nx2 = " + str(x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("x+iy и x-iy")
