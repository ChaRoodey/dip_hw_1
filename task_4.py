'''Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы:'''

d = int(input('Введите глубину ямы: '))

for i in range(d, 0, -1):
    for j in range(d, i - 1, -1):
        print(j, end='')

    print((i - 1) * 2 * '.', end='')

    for k in range(i, d + 1):
        print(k, end='')

    print()