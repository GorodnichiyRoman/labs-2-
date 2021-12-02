f1 = 1
f2 = 1

while (f2 < 10000):
    f3 = f1 + f2
    f1 = f2
    f2 = f3

    if (f2 >= 1000):
        f4 = str(f2)
        print(len(f4), " Элемента")
        break
