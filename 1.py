#1

print('задача № 1\n')
print('Введите трехзначное число:\n')55
value=int(input())

a = value // 100
b = value // 10 % 10
c = value % 10

result_sum = a + b + c
result_mult = a * b *c

print(f'сумма = {result_sum}, произведение = {result_mult}')

#2
print('\n задача № 2\n')
a = 5
b = 6
print(f'{bin(a)} & {bin(b)} = {bin(a & b)}')
print(f'{bin(a)} | {bin(b)} = {bin(a | b)}')
print(f'{bin(a)} ^ {bin(b)} = {bin(a ^ b)}')
print(f'Побитовый сдвиг вправо числа 5 на 2 знака = {bin(a >> 2)}')
print(f'Побитовый сдвиг влево числа 5 на 2 знака = {bin(b << 2)}')

#3
print('\n задача № 3\n')
print('введите координаты точки A(x,y):\n')
x1, y1 = float(input()), float(input())

print('введите координаты точки B(x,y):\n')
x2, y2 = float(input()), float(input())

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

sign = '-' if b < 0 else '+'
print(f'y = {k} * x {sign} {abs(b)}')

#4
print('\n задача № 4\n')
from random import randint
print('Введите границы символьного диапазона:\n')
a, b = ord(input()), ord(input())
print(chr(randint(a,b)))

#5
print('\n задача № 5\n')
print('Введите 2 строчные буквы английского алфавита')
a, b = ord(input('Первая буква: ')), ord(input('Вторая буква: '))
a1 = a - ord('a') + 1
b1 = b - ord('a') + 1
print(f'Буква {chr(a)} - {a1} буква алфавита')
print(f'Буква {chr(b)} - {b1} буква алфавита')
print(f'Между ними {abs(a-b)-1} символов')

#6
print('\n задача № 6\n')
print('Введите номер буквы английского алфавита:\n')
letter = int(input())
if letter <= 26:
  result = ord('a') + letter - 1
  print(chr(result))
else:
  print('В английском алфавите 26 букв!')

#7
print('\n задача № 7\n')
print('Введите длины треугольника:\n')
a, b, c = int(input()), int(input()), int(input())
if a + b > c and b + c > a and c + a > b:
  print(f'Треугольник со сторонами {a}, {b} и {c} существует ')
  if a==b==c:
    print('и является равносторонним')
  elif a == b or b == c or a == c:
    print('и является равнобедренным')
  else:
    print('и является разносторонним')
else:
  print(f'Существование треугольника со сторонами {a}, {b} и {c} не возможно')

#8
print('\n задача № 8\n')
print('Введите год\n')
year = int(input())
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
  print(f'{year} год является високосным')
else:
  print(f'{year} год не високосный')

#9
print('\n задача № 9\n')
print('Введите 3 разных числа:\n')
a, b, c = int(input()), int(input()), int(input())
if  b < a < c or c < a < b:
  print('среднее число - ', a)
elif a < b < c or c < b < a:
  print('среднее число - ', b)
else:
  print('среднее число - ', c)