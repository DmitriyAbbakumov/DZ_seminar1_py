# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input("Введите цифру дня недели: "))
if n < 1 or n > 7:
    print("нет такого дня недели")
elif n > 5:
    print("Выходной")
else:
    print("Будний")
