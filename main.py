def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ввод от пользователя
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Вызов функции для нахождения НОД
result = nod(num1, num2)

print(f"Наибольший общий делитель {num1} и {num2} = {result}")
