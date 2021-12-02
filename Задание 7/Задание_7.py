
a = int(input("Введите 1 сторону треугольника: "))
b = int(input("Введите 2 сторону треугольника: "))
c = int(input("Введите 3 сторону треугольника: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Error")
elif a == b or b == c or c == a:
    print("True")
elif a + b < c or a + c < b or c + b < a:
    print("False")