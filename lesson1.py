
print("hello world")
print(6)
age = 9     # возраст
print(age)
print('Возраст равен: ', age)

print(2 - 8 * (4 + 1))
print(2 ** 3)  # возведение в степень
print(4 // 3)  # целочисленное деление
print(6 % 2)  # остаток от деления
print(123 // 100)
print(6 % 2)

# свойство четности : i % 2 = 0

age = 8  # int
b = float(age)
print(float(age))
print(float(8))
c = 9.099999
print(int(c))
st = str(c)  # превращает аргумент в строку
print(type(st))
print(bool(0))
print(bool(''))
print(bool(None))

print('Название книги : "Три товарища"')

answer = int(input('Введите ваш возраст: '))  # всегда возвращает строку
# answer = int(answer)
print(type(answer))

a = 8   # операция присвоения
b = 'yes'
if a == 8 and b == 'yes':  # проверка равенства > <  >= <= !=
    print('ok')
    a = a + 8
if a == 8 or b == 'yes':
    print('ok')
# not in is

pasw = '123'
code_true = 'koko'
answ = input('Введите пароль: ')

if answ == pasw:
    code = input()
    if code == code_true:
        print('Верный пароль')
else:
    print('Неверный пароль')

color = input()
if color == 'red':
    print('красный')
elif color == 'green':   # else if
    print('зеленый')
elif color == 'blue':
    print('синий')
else:
    print('такого цвета нет')


num = int(input('Введите число: '))
while num > 0:
    print(num)
    num = num - 1  # num -= 1
print('Готово')

i = 0
while True:
    i += 1
    if i >= 10:
        break   # принудительный выход из цикла
    if i % 2 == 0:
        continue  # переход к след итерации
    print(i)

age = 98
name = 'Kate'
print('your name is', name, 'your age = ', age)
print('your name is %s, your age = %d' % (name, age))
# print('your name is %s, your age = %d' %(age, name))  #decimal string
print('your name is {}, your age = {}' .format(name, age))
print('third el = {2}, second el = {1}, first el = {0}' .format('el1', 'el2', 'el3'))
print(f'your name is {name}, your age = {age}')
