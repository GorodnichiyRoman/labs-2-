n = int(input('Введите натуральное число число: '))
while n <= 0:
    print("n не может быть меньше 0: ")

a = []
b = []

for l in range(10, 1000):
    x, y, z, j = l % 10, (l % 100) // 10, l // 100, l // 10
    if l > 99:
        if (x ** 3 + y ** 3 + z ** 3 == n) and not x in a and not y in a and not z in a:
            print('{}³+{}³+{}³={}'.format(x, y, z, n))
            a.append(x)
            a.append(y)
            a.append(z)
else:
    print("No such combinations!")
