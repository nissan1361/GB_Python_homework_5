# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))


def step_func(a, b):
    if b == 0:
        return 1

    return a * step_func(a, b - 1)


print(step_func(a, b))