number = int(input("Введите количество слагаемых: "))

p = 0

for i in range(1, number + 1, 2):
    p += 4 / i - 4 / (i+2)

print("Приблизительное значение будет pi = " + str(p))
