# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

while True:
    try:
        num = int(input('Введите количество предприятий: '))
        break
    except ValueError:
        print('Вы ввели некорректные данные\n')
        continue

i = 1
name = []
income = []

while i <= num:

    while True:

        try:
            name.append(str(input('\nВведите название {} предприятия: '.format(i))))
            break
        except ValueError:
            print('Вы ввели некорректные данные\n')
            continue

    j = 1
    spam = []
    while j <= 4:

        while True:
            try:
                spam.append(float(input('Введите прибыль за {} квартал: '.format(j))))
                break
            except ValueError:
                print('Вы ввели некорректные данные\n')
                continue

        j += 1

    income.append(spam)
    i += 1

dict_all = dict(zip(name, income))

new_dict = {}
summ_all = 0

print('*' * 50)

for index, value in dict_all.items():

    new_dict[index] = sum(value)
    summ_all += sum(value)
    print('\n У {} прибыль за год составляет {}'.format(index, sum(value)))

average_income = summ_all / num

print('*' * 50)
print(' Средняя прибыль по всем предприятиям = ', average_income)
print('*' * 50)

str_less = []
str_more = []
str_equally = []

for index, value in new_dict.items():

    if value < average_income:
        str_less.append(index)
    elif value > average_income:
        str_more.append(index)
    else:
        str_equally.append(index)

if str_more is not None:
    print('\nПрибыль выше среднего у предприятий: ', str_more)
if str_less is not None:
    print('Прибыль ниже среднего у предприятий: ', str_less)
if str_equally is not None:
    print('Прибыль равно среднему у предприятий: ', str_equally)
