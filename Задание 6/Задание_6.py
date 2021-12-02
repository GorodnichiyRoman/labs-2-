age = int(input("Введите возраст: "))

if age > 100:
    input(" Столько жить нельзя !")
if age < 0:
    input(" Возраст не может быть отрицательным ! ")

a1 = age % 10
a2 = age % 100

if (a1 == 1 and a2 != 11):
    print(str(age) + " год")
elif (a1 >= 2 and a1 <= 4 and (a2 < 10 or a2 >= 20)):
    print(str(age) + " года")
else:
    print(str(age) + " лет")
