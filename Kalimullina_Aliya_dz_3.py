#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
print('Задача № 1\n')

a = [0] * 8

for i in range(2,100):
  for j in range(2,10):
    if i % j == 0:
      a[j-2] += 1

i = 0
print('В диапазоне натуральных чисел от 2 до 99:')
while i < len(a):
  print(f'кратны {i + 2} - {a[i]} чисел')
  i += 1

#2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
print('\nЗадача № 2\n')

import random

first = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {first}')

second = []
for i in first:
  if i % 2 == 0:
    second.append(first.index(i))
print(f'Индексы четных элементов первого массива:  {second}')

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
print('\nЗадача № 3\n')

import random

first = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до - {first}')

max = first[0]
min = first[0]

for i in first:
    if i > max:
        max = i
    elif i < min:
        min = i
min_idx = first.index(min)
max_idx = first.index(max)
print(f'элементы {first[max_idx]} и {first[min_idx]} поменяем местами:')
first[min_idx], first[max_idx] = first[max_idx], first[min_idx]
print(f'Массив после - {first}')


# 4. Определить, какое число в массиве встречается чаще всего.
print('\nЗадача № 4\n')

from random import random

arr = [int(random()*5) for i in range(10)]
print(arr)
q = 0
idx = 0
set_arr = set(arr)
for i in set_arr:
  if q < arr.count(i):
    q = arr.count(i)
    idx = i
print(f'Число {idx} встречается наибольшее количество раз ({q})')
  

#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
print('\nЗадача № 5\n')

import random

arr = [random.randint(-99, 99) for _ in range(15)]
print(f'Массив: {arr}')

idx = 0

for i in arr:
    if arr[idx] > i:
        idx = arr.index(i)

if arr[idx] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицательный элемент arr[{idx}]={arr[idx]} ')

#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
print('\nЗадача № 6\n')

import random

arr = [random.randint(0, 99) for _ in range(10)]
print(arr)
max = arr[0]
min = arr[0]

for i in arr:
  if i > max:
    max = i
  elif i < min:
    min = i
min_idx = arr.index(min)
max_idx = arr.index(max)
sum = 0
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
if max_idx - min_idx > 1:
  for i in range(min_idx+1, max_idx):
    sum += arr[i]
else: sum = 0
print(f'Сумма элементов, находящихся между {min} и {max} равна {sum}')

#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
print('\nЗадача № 7\n')

import random

arr = [random.randint(0, 10) for _ in range(10)]
print(arr)
sort_list = []
sort_list.extend(arr)
sort_list.sort()

print(f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}')


#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
print('\nЗадача № 8\n')

matrix = []

for i in range(5):
    matrix.append([])
    sum = 0
    for j in range(3):
        el = int(input(f'{i+1} строка {j+1} столбец: '))
        sum += el
        matrix[i].append(el)

    matrix[i].append(sum)

for a in matrix:
    print(('{:>4d}' * 4).format(*a))

#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
print('\nЗадача № 9\n')

import random

matrix = []
r,c = int(input('Число строк: ')),int(input('Число столбцов: '))

for i in range(r):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(c)])

min_el = []
min_el.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_el[i]:
            min_el[i] = j
        i += 1

print()
print('Минимальные элементы столбцов:\n')
print(('{:4d} ' * len(min_el)).format(*min_el))
print()

min_el.sort(reverse=True)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {min_el[0]}')