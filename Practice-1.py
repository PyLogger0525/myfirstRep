#print("Введите год: ")
#Y= int(input())

#if Y % 4 == 0 or Y % 100==0 and Y % 400 == 0:
 #   print('Год високосный')
#else:
#    print('Год не високосный')

#a=int(input('Введите число: '))
#b=int(input('Введите число: '))
#g =  a if a>b else b
#print('Наибольшее число: ', g)

# prices=int(input())
# for percentage in prices:
#     if int(prices) == 5000:
#         percentage == int(5)
#         d_price=prices*percentage
#         print(f"{percentage:.0%}")
#         print('Сумма с учетом скидки: ', d_price)

# mpg = int(input('MPG' ))
# lkm = int(input('L/100 km '))
# Km = mpg * 1.06
# print(Km, 'L/100km')

# password = "dgh36gh7"
# answer = input()
# if answer == password:
#     print(True)
# else

# N = str(16)
# R = N[0]
# R_N = int(R)
# print(R_N % 2 ==0)

# password = "dgh36gh7"
# answer = input()
# if answer == password:
#     print("Пароль верен! Добро пожаловать.")
# else:
#     print("Вы ввели неверный пароль")

# mx = 0
# s = 0
# x = int(input())
# if x < 0:
#     s = x
# b = 7
# b /= b
# if x > mx:
#     mx = x
# print(s)
# print(mx)

# name = input(" ")
# name_x = 'Арарат'
# if name != name_x:
#     print('Нашлась подделка!', name)
# else:
#     print('Коньяк {name} не подделка')

# cost = int(input())
# m = 2500
# if cost <= int(m):
#     print('Вы можете купить эти кроссовки!')
# else:
#     print('Увы, кроссовки слишком дорогие!')

# x = input("enter number: ")
#
# if x:
#     x = int(x) * 2
# else:
#     x = None
#     print(x)

# Dedline = False
# t = 17
# if t >= 15 and not Dedline:
#     print('идем гулять')
# else:
#     print('сидим дома')

# a = int(input())
# two = int(input())
# resoult = a % 2 == 0 and two % 2 ==0
# if resoult:
#     print(True)
# if not resoult:
#     print(False)

# one = int(input())
# two = int(input())
# result = one % 2 == 0 and two % 2 == 0
# print(result)

# a = int(input())
# speed = 15
# if 1< a <4:
#     print('weak')
# if a <= 0:
#     print('Error')

# a = int(input())
# b = int(input())
# c = int(input())
# result = a if a < 45 or b if b <45 or c < 45:
#     print(result)
# if a < 45:
#     print(a)
# elif b < 45:
#     print(b)
# else:
#     print(c)

# a = int(input())
# # result = a if a > b else b
# result = -1 > a < -10 or 2 > a < 15
# print(result)

# number = int(input())
# string = str(number)
# if string == string[::-1]:
#     print("Number - палиндром")
# else:
#     print("Number - не палиндром")


# isRain = True #Дождь будет
# isNotRain = False #Дождя не будет
# temperature =  str(input('Температура больше 20 и меньше 30 градусв? '))
# if temperature == 'Да':
#     isRain = str(input('Есть осадки? '))
#     if isRain == 'Да':
#         print('Футблку, шорты и дождевик')
#     else:
#         print('Футблку и шорты')
# else:
#     temperature = str(input('Температура больше 0 градусов? '))
#     if temperature == 'Нет':
#         print('Пуховик')
#     else:
#         isRain = str(input('Есть осадки? '))
#         if isRain == 'Нет':
#             print('Пальто')
#         else:
#             isStrongRain = str(input('Осадки сильные? '))
#             if isStrongRain == 'Нет':
#                 print('Пальто и дождевик')
#             else:
#                 print('Пальто и резинвые сапоги')

# #Запрашиваем ввод температуры
# temperature = int(input("Input temperature: "))
# #для указания начальных статусов дождливости воспользуемся False или None
# rainy = None
# heavyRain = None
# #если температура <0 то про дождь спрашивать бессмысленно
# if temperature > 0:
#    rainy = input("Is rainy: ") == "yes"
# #если идет дождь спросим насколько он серьезный
#    if rainy:
#        heavyRain = input("Is heavy rain: ") == "yes"
# #реализуем логику по схеме
# decision = "Не решил что брать. Останусь дома."
# if (temperature) > 20 and (temperature < 30) :
#    if rainy:
#        decision = "Взять футболку шорты и дождевик"
#    else:
#        decision = "Взять футболку и шорты"
# elif temperature > 0:
#    if rainy:
#        if heavyRain:
#            decision = "Взять пальто, резиновые сапоги и зонт"
#        else:
#            decision = "Взять пальто и дождевик"
#    else:
#        decision = "Взять пальто"
# else:
#    decision = "Взять пуховик"
# #Выведем наше решение на экран
# print(decision)

# x=0
# i = 1
# while x ** 2 <= 1000:
#     x+=i
#     i += 1
# print(x)

# n = 10
# i = 1
# while i ** 2 < n:
#     i += 1
# print(i)

# n = 10
# i = 0
# while i < n:
#
#     print('Hello')
#     i = i + 1

# n = 10000
# i = 2
# r = 1
# while i ** r < n:
#     r += 1
#     print(r)

# start_cash = 1000
# target_cash = 3000
# proc = 0.08
# years = 0
# while start_cash < target_cash:
#     start_cash *= (1 + proc)
#     years += 1
# print(years)

# employee = 5
# i = 1
# while i < employee:
#     if i > 1:
#         print('There are', i, 'people in the department')
#     if i == 1:
#         print('There are', i, 'people in the department')
#     i += 1

# S = 0  # заводим переменную счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# my_list= [5, 9, 19]  # определяем итерируемый объект
# for element in my_list: # подставляем его в шаблон для цикла и записываем имя переменной, которое будет использовано для каждого элемента этого объекта. В данном случае это element
#     print('Element', element)

# p = 0
# N = 5
# for i in range(1, N + 1):
#     print("Значение разности на предыдущем шаге: ", p)
#     print("Текущее число: ", i)
#     N = N * i
#     print("Значение суммы после умножения: ", N)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: произведение чисел равно = ", N)

# n = 4
# for i in range(n):
#     for j in range(1, i + 2):
#         print(j, end = '')
#     print()
# n = 3
# for i in range(1, n +1):
#     print(str(i) * i)
#
# ROWS = 3
# COLS = 2
#
# matrix = [
#     [1, 2]
#    ,[3, 4]
#    ,[5, 6]
# ]
#
# for i in range(ROWS):
#    for j in range(COLS):
#        print(matrix[i][j], end = " ")
#    print()
#
# matrix = [
#     [1, 2]
#    ,[3, 4]
#    ,[5, 6]
# ]
#
# for row in matrix:
#    for element in row:
#        print(element, end = " ")

# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements:", min_value_rows) # минимальные элементы
# print("Their indices:", min_index_rows) # их индексы
# print("Maximal elements:", max_value_rows) # максимальные элементы
# print("Their indices:", max_index_rows) # их индексы

# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]]
# max_value_rows = []
# max_index_rows = []
# for row in test_matrix:
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements:", max_value_rows) # минимальные элементы
# print("Their indices:", max_index_rows) # их индексы

# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]]
# num_lines = len(test_matrix)
# cnt = 0
# for line in test_matrix:
#     if len(line) == num_lines:
#         cnt += 1
# print(num_lines == cnt)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i in range(len(list_)):
#     if list_[i] < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#    if value < 0:
#        print("Отрицательное число: ", value)
#        index_negative = i  # перезаписываем значение индекса
#        print("Новый индекс отрицательного числа: ", index_negative)
#    else:
#        print("Положительное число: ", value)
#    print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
# text = text.lower() # привели все к нижнему регистру
# text = text.replace("\n", "") #убрали символы перевода строки
# text = text.split()
# count = {}
# for word in text:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
#         for char, cnt in count.items():
#             print(f"Символ {char} встречается {cnt} раз")

# упражнение 5
# b1 = 0.10
# b2 = 0.25
# b3 = float(input('Количество сданных бутылок до 1 л: '))
# b4 = float(input('Количество сданных бутылок больше 1 л: '))
# cash = (b1 * b3) + (b2 * b4)
# all_cash = round(cash, 2)
# print('Вы получите', all_cash, '$')


#Упражнение 6
# food = float(input('Введите сумму зааказа: '))
# nalog = 0.13
# chai = 0.18
# nal1 = round((food * nalog), 2)
# ch1 = round((food * chai), 2)
# all1 = round((food + nal1 + ch1), 2)
# print('Общая сумма чека:', all1)
# print('Сумма налога:', nal1)
# print('Сумма чаевых:', ch1)



