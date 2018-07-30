# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

new_num1 = []
new_num2 = []
sum_nums = []
mult_nums = []

# Вваодим числа, провреяем правильность ввода и делаем новые списки в десятичном виде

while True:

    c = 0

    num1 = list(input('\nВведите первое шестнадцатеричное число (буквы должны быть заглавными): '))

    for i in num1:

        if i == 'A':
            new_num1.append('10')
        elif i == 'B':
            new_num1.append('11')
        elif i == 'C':
            new_num1.append('12')
        elif i == 'D':
            new_num1.append('13')
        elif i == 'E':
            new_num1.append('14')
        elif i == 'F':
            new_num1.append('15')
        else:
            new_num1.append(i)

        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != 'A' and i != 'B' and i != 'C' and i != 'D' and i != 'E' and i != 'F':
            print('Вы ввели не корректное значение шестнадцатиричное числа')
            c += 1
            break
        else:
            continue

    if c != 0:
        continue
    else:
        break

while True:

    c = 0

    num2 = list(input('\nВведите второе шестнадцатеричное число (буквы должны быть заглавными): '))

    for i in num2:

        if i == 'A':
            new_num2.append('10')
        elif i == 'B':
            new_num2.append('11')
        elif i == 'C':
            new_num2.append('12')
        elif i == 'D':
            new_num2.append('13')
        elif i == 'E':
            new_num2.append('14')
        elif i == 'F':
            new_num2.append('15')
        else:
            new_num2.append(i)

        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != 'A' and i != 'B' and i != 'C' and i != 'D' and i != 'E' and i != 'F':
            print('Вы ввели не корректное значение шестнадцатиричное числа')
            c += 1
            break
        else:
            continue

    if c != 0:
        continue
    else:
        break

i = 0

# Переворачиваем список и добиваем нулями нехватающие элементы, для сложения

new_num1 = new_num1[::-1]
new_num2 = new_num2[::-1]

# Добиваем более короткий список нулями, для сложения
if len(new_num1) < len(new_num2):
    max_len = len(new_num2)
    min_len = len(new_num1)
    difference = len(new_num2) - len(new_num1)
    while i < difference:
        new_num1.append('0')
        i += 1
else:
    max_len = len(new_num1)
    min_len = len(new_num2)
    difference = len(new_num1) - len(new_num2)
    while i < difference:
        new_num2.append('0')
        i += 1

print(num1, num2)
print(new_num1, new_num2)

# Складываем

i = 0
b = 0

while i < max_len:

    if b > 0:
        a = int(new_num1[i]) + int(new_num2[i]) + 1
    else:
        a = int(new_num1[i]) + int(new_num2[i])

    if a <= 9:
        sum_nums.append(a)

    elif a > 9:

        b = a - 16

        if b > 0:

            a = a - b

            if b == 10:
                sum_nums.append('A')
            elif b == 11:
                sum_nums.append('B')
            elif b == 12:
                sum_nums.append('C')
            elif b == 13:
                sum_nums.append('D')
            elif b == 14:
                sum_nums.append('E')
            elif b == 15:
                sum_nums.append('F')
            else:
                sum_nums.append(b)

        else:

            if a == 10:
                sum_nums.append('A')
            elif a == 11:
                sum_nums.append('B')
            elif a == 12:
                sum_nums.append('C')
            elif a == 13:
                sum_nums.append('D')
            elif a == 14:
                sum_nums.append('E')
            elif a == 15:
                sum_nums.append('F')
            else:
                sum_nums.append(a)

        if (i + 1) == max_len and b > 0:
            sum_nums.append('1')

    i += 1

# Переворачиваем списки
sum_nums = sum_nums[::-1]
mult_nums = mult_nums[::-1]

#Выводим ответы
print('=' * 50)
print('Результат сложения = ', end='')
for i in sum_nums:
    print(i, end='')

