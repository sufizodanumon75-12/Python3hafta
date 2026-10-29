# import math
# from math import floor, ceil

# # res=math.ceil(4.4)
# # res=math.floor(4.9)
# # res=floor(4.3)
# # res=ceil(4.3)
# # res=math.sqrt(81)
# res=math.pi
# # res=math. factorial(4)
# # res=math.pow(3.5,3)
# print(res)


# #import datetime
# from datetime import datetime, date, timedelta

# now=datetime.now()
# today=date.today()
# tomorow=today+timedelta(days=1)
# yesterday=today-timedelta(days=1)

# print(yesterday)
# print(today)
# print(tomorow)

# print(now.strftime('48'))

# print(now.strftime('%A°'))

# text='27-10-2026'
# res=datetime.strptime(text, '%d-%m-%Y')

# print(res)

# import random



# res=random.randint(100000,999999)
# res=random. random()
# res=random.choices(['Qobil','Alijon', 'Arsen','Numon','Dilnoza'], weights=[10,7,8,35,40],k=1)
# print(res)
# res=random.choices(['Qobil','Alijon','Arsen','Numon','Dilnoza'],k=3)
# res=random.choice(['Qobil','Alijon','Arsen', 'Numon','Dilnoza'])

# lst=[1,2,3,4,5]
# random. shuffle(lst)

# print(lst)

# print(res)


# -------------------------------------------Class work------------------------------------
# import random
# random.randint()
# 1. Угадай число
# Компьютер загадывает случайное число от 1 до 10. Пользователь должен его угадать.
# res=random.randint(1,10)
# print(res)
# 2. Случайный пароль
# Сгенерируйте 8 случайных цифр от 0 до 9 и соедините их в строку.
# Пример:
# 58410397

# import random

# rakam = ''
# for i in range(8):
#     rakam += str(random.randint(0, 9))
# 3. Кубик
# Сымитируйте бросок двух игральных кубиков и выведите их сумму.
# Пример:
# Первый: 4
# Второй: 6
# Сумма: 10
# pervyi = random.randint(1, 6)
# vtoroi = random.randint(1, 6)

# print('Первый:', pervyi)
# print('Второй:', vtoroi)
# print('Сумма:', pervyi + vtoroi)
# 4. Лотерея
# Сгенерируйте счастливое число от 100000 до 999999.
# random.random()
    # import random

    # chislo = random.randint(100000, 999999)
    # print(chislo)
# 5. Вероятность дождя
# Сгенерируйте число от 0 до 1.
# Если оно меньше 0.3 — вывести:
# Сегодня дождь.
# иначе:
# Дождя не будет.
# if random.random() < 0.3:
#     print('Iruz boronay zontikotona bgiren')
# else:
#     print('Iruz boron nest mepazi ay garmira')
# 6. Монетка
# Используя только random.random(), реализуйте подбрасывание монеты.
# Орел
# или
# Решка
# if random.random() < 0.5:
#     print('50 diram')
# else:
#     print('Nishon')
# 7. Скидка
# Если случайное число меньше 0.15 — пользователь получает скидку 20%.
# Иначе скидки нет.
# random.randrange()
# if random.randrange(100) < 15:
#     print('Скидка 20%')
# else:
#     print('Скидки нест брен хонотон')
# 8. Четные числа
# Выведите случайное четное число от 2 до 100.
# chislo = random.randrange(2, 101, 2)
# print(chislo)
# 9. Кратные пяти
# Выведите случайное число от 10 до 100, кратное 5.
# chislo = random.randrange(0, 101, 5)
# print(chislo)
# 10. Шаг
# Получить случайное число от 50 до 100 с шагом 7.
# random.choice()
# chislo = random.randrange(0, 101, 7)
# print(chislo)
# 11. Случайный фрукт
# Есть список фруктов.
# Выведите случайный фрукт.
# ["Яблоко", "Апельсин", "Банан", "Манго", "Киви"]
# frukty = ["Яблоко", "Апельсин", "Банан", "Манго", "Киви"]
# print(random.choice(frukty))
# 12. Выбор победителя
# Есть список участников конкурса.
# Выберите случайного победителя.
# uchastniko = ["Аli", "Bilol", "vali", "Gafur"]
# print("Brid:", random.choice(uchastniko))
# 13. Цитата дня
# Есть список цитат.
# Каждый запуск программы должен показывать одну случайную цитату.
# random.choices()
# citata = [
#     "Ученье — свет.",
#     "Дорогу осилит идущий.",
#     "Маленькие шаги ведут к большим целям."
# ]
# print(random.choices(citata, k=1)[0])
# 14. Случайные оценки
# Сгенерируйте список из 20 случайных оценок.
# [5, 4, 3, 5, 2, ...]
# Используйте
# [2,3,4,5]
# baho = random.choices([2, 3, 4, 5], k=20)
# print(baho)
# 15. Генератор PIN-кодов
# Создайте PIN длиной 6 цифр.
# 483017
# pin = ''.join(random.choices("0123456789", k=6))
# print(pin)
# 16. Генератор ДНК
# Используя
# ["A","T","G","C"]
# dnk = ''.join(random.choices(["A", "T", "G", "C"], k=30))
# print(dnk)
# сгенерируйте последовательность длиной 30 символов.
# random.sample()
# 17. Лотерея
# Из списка чисел от 1 до 49 выберите 6 различных чисел.
# rakam = random.sample(range(1, 50), 6)
# print(rakam)
# 18. Команда
# Есть список из 20 студентов.
# Выберите случайных 5 человек без повторений.
# random.shuffle()

# 19. Перемешай колоду
# Создайте список карт
# ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# Перемешайте его и выведите.
# 20. Викторина
# Есть список вопросов.
# Перед началом игры перемешайте их случайным образом и выведите все вопросы по порядку.
# Бонус (сложная задача)
# Создайте игру "Камень, ножницы, бумага".
# Используйте:
# random.choice() — выбор компьютера;
# цикл while;
# подсчет побед пользователя и компьютера;
# игра идет до 3 побед одной из сторон;
# после окончания предложить сыграть еще раз.





# -------------------------------------------------Home work-----------------------------------
# Текущее время

# Импортируйте модуль `time` и выведите Unix timestamp текущего момента.

# import time

# print(time.time())

# ### 2. Пауза

# Выведите:

# ```text
# Start
# import time

# print("Start")
# time.sleep(2)
# print("End")
# 3. Обратный отсчёт

# Создайте программу:


# 3
# 2
# 1
# Start!
# Между каждым числом должна быть пауза в 1 секунду.

# import time

# for rakam in range(3, 0, -1):
#     print(rakam)
#     time.sleep(1)

# print("Start!")

# ### 4. Обратный отсчёт от 10

# Сделайте обратный отсчёт:


# 10
# 9
# 8
# ...
# 1
# GO!


# Между числами должна быть пауза 1 секунда.

# import time

# for rakam in range(10, 0, -1):
#     print(rakam)
#     time.sleep(1)

# print("GO!")

# ### 5. Пауза 0.5 секунды

# Выведите числа от 1 до 10.

# Между каждым числом сделайте паузу 0.5 секунды.

# import time

# for rakam in range(1, 11):
#     print(rakam)
#     time.sleep(0.5)

# ### 6. Измерение времени

# Измерьте, сколько секунд выполняется цикл от 1 до 1 000 000.

# Используйте:


# time.time()


# import time

# начало = time.time()

# for число in range(1, 1_000_001):
#     pass

# конец = time.time()
# print("Raft:", конец - начало)

# ### 7. Измерение sleep

# Создайте программу, которая:

# 1. запоминает время;
# 2. делает sleep(2);
# 3. снова получает время;
# 4. выводит, сколько секунд прошло.

# import time

# начало = time.time()
# time.sleep(2)
# конец = time.time()

# print("Raft:", конец - начало)

# ### 8. Таймер

# Попросите пользователя ввести количество секунд:


# Введите количество секунд: 5


# После этого программа должна каждую секунду выводить оставшееся время.

# import time

# sekund = int(input("Sekunda bmon: "))

# for mond in range(sekund, 0, -1):
#     print(mond)
#     time.sleep(1)

# print("Vakt tamom shid!")

# ### 9. Таймер с сообщением

# Пользователь вводит количество секунд.

# После окончания таймера выведите:


# Время вышло!


# import time

# sekund = int(input("Sekunda bmon: "))

# for mond in range(sekund, 0, -1):
#     print(mond)
#     time.sleep(1)

# print("Vakt tamom shid!")

# ### 10. Загрузка

# Сымитируйте загрузку:


# Loading.
# Loading..
# Loading...
# Loading.
# Loading..
# Loading...

# import time

# for dots in range(1, 4):
#     print("Loading" + "." * dots)
#     time.sleep(0.5)

# for dots in range(1, 4):
#     print("Loading" + "." * dots)
#     time.sleep(0.5)

# Каждое изменение должно происходить через 0.5 секунды.

# ---

# # 🟢 Уровень 2 — Основы random

# ### 11. Случайное число

# Сгенерируйте случайное число от 1 до 10.

# import random

# rakam = random.randint(1, 10)
# print(rakam)

# ### 12. Случайное число от 1 до 100


# Выведите случайное число от 1 до 100.

# import random

# rakam = random.randint(1, 100) 
# print(rakam)

# ### 13. Чётное случайное число

# Сгенерируйте случайное число от 1 до 100.

# Если число чётное — выведите:


# # Чётное


# # Иначе:


# # Нечётное


# # import random

# # rakam = random.randint(1, 100)

# # if rakam % 2 == 0:
# #     print("Guft")
# # else:
# #     print("Tok")

# # ### 14. Угадай число

# # Компьютер загадывает число от 1 до 10.

# # Пользователь должен угадать число.

# # import random

# # raqami_pinon = random.randint(1, 10)
# # takhmin = int(input("Rakam ay 1 to 10: "))

# # if takhmin == raqami_pinon:
# #     print("Durustay bh bgard!")
# # else:
# #     print("Inami bago shiday:", raqami_pinon)

# # ### 15. Угадай число — 3 попытки

# # Компьютер загадывает число от 1 до 20.

# # У пользователя есть только 3 попытки.

# # import random

# # raqami_pinon = random.randint(1, 20)

# # for kushish in range(3):
# #     takhmin = int(input("Rakam ay 1 to 20: "))

# #     if takhmin == raqami_pinon:
# #         print("Durustay bh bgard!")
# #         break
# #     else:
# #         print("Hato kadi.")

# # if takhmin != raqami_pinon:
# #     print("Tamom brat ina rakamipinoni:", raqami_pinon)

# # ### 16. Орёл или решка

# # Создайте программу, которая случайно выбирает:


# # Орёл
# # Решка


# # import random

# # natija = random.choice(["50 diram", "nishon"])
# # print(natija)

# # ### 17. Бросок кубика

# # Симулируйте бросок обычного кубика.

# # Возможные значения:


# # 1 2 3 4 5 6


# # import random

# # rakam = random.randint(1, 6)
# # print(rakam)

# # ### 18. Два кубика

# # Сгенерируйте два случайных значения кубика.

# # Выведите:


# # Кубик 1: 4
# # Кубик 2: 6
# # Сумма: 10


# # import random

# # kubik_1 = random.randint(1, 6)
# # kubik_2 = random.randint(1, 6)

# # print("Kubik 1:", zari_1)
# # print("Kubik 2:", zari_2)
# # print("Gam:", kubik_1 + kubik_2)

# # ### 19. Случайный пароль из цифр

# # Создайте пароль длиной 6 символов, используя случайные цифры.

# # import random

# # ramz = "".join(random.choices("0123456789", k=6))
# # print(ramz)

# # ### 20. Случайный PIN

# # Создайте случайный PIN-код из 4 цифр.

# # import random

# # pin = "".join(random.choices("0123456789", k=4))
# # print(pin)

# # # 🟢 Уровень 3 — random.choice()

# # ### 21. Случайное имя

# # Создайте список из 5 имён.

# # С помощью random.choice() выберите случайное имя.

# # import random

# # nomho = ["Ali", "Bilol", "Vali0", "Gafur", "Davlat"]
# # print(random.choice(nomho))

# # ### 22. Случайный цвет

# # Создайте список:


# # ["red", "green", "blue", "yellow", "black"]


# # Выберите случайный цвет.

# # import random

# # rangho = ["red", "green", "blue", "yellow", "black"]
# # print(random.choice(rangho))

# # ### 23. Случайный фрукт

# # Создайте список из 5 фруктов и выберите один случайно.

# # import random

# # mevaho = ["Себ", "Апелсин", "Банан", "Манго", "Киви"]
# # print(random.choice(mevaho))

# # ### 24. Случайная страна

# # Создайте список из 10 стран.

# # Выведите случайную страну.

# # import random

# # kishvarho = [
# #     "Tojikiston", "Rusiya", "Qazoqiston", "Uzbekiston", "Chin",
# #     "Japon", "Faronsa", "Italiya", "Misr", "Braziliya"
# # ]
# # print(random.choice(kishvarho))

# # ### 25. Случайный студент

# # Создайте список студентов.

# # Программа должна случайно выбрать студента для ответа.

# # import random

# # fanho = ["Matematika", "Tarikh", "Fizika", "Biologiya", "Informatika"]
# # print(random.choice(fanho))

# # ### 26. Случайный предмет

# # Создайте список школьных/университетских предметов.

# # Выберите случайный предмет.

# # import random

# # dastaho = ["Dastai A", "Dastai B", "Dastai C", "Dastai D"]
# # print(random.choice(dastaho))

# # ### 27. Камень, ножницы, бумага

# # Создайте игру:


# # Камень
# # Ножницы
# # Бумага


# # Компьютер должен сделать случайный выбор.

# # import random

# # intikhobi_kompyuter = random.choice(["Sang", "Qaychi", "Kogaz"])
# # print("Kompyuter intikhob kard:", intikhobi_kompyuter)

# # ### 28. Случайная команда

# # Создайте список:


# # Team A
# # Team B
# # Team C
# # Team D


# # Случайно выберите команду.

# # import random

# # dastaho = ["Dastai A", "Dastai B", "Dastai C", "Dastai D"]
# # print(random.choice(dastaho))

# # ### 29. Случайное животное

# # Создайте список из 10 животных.

# # Случайно выберите животное.

# # import random

# # hayvonho = [
# #     "Gurba", "Sag", "Asp", "Gov", "Sher",
# #     "Palang", "Gurg", "Khirs", "Khargush", "Rubah"
# # ]
# # print(random.choice(hayvonho))

# # ### 30. Случайный вопрос

# # Создайте список из 10 вопросов.

# # Программа должна случайно выбрать вопрос для пользователя.

# # import random

# # savolho = [
# #     "Rangi dustdoshtai shumo chi ast?",
# #     "Kadom khurokro dust medored?",
# #     "Ba kujo safar kadan mekhohi?",
# #     "Kadom kitobro mekhoni?",
# #     "Filmi dustdoshtai shumo kadom ast?",
# #     "Kadom hayvonro dust medored?",
# #     "Bo chi mashgul sidana dust medori?",
# #     "Kadom fan ba shumo maqul ast?",
# #     "Kadom musikиrо gush mekni?",
# #     "Orзуи shumo chi ast?"
# # ]
# # print(random.choice(savolho))

# Уровень 4 — random.shuffle()

# ### 31. Перемешать числа

# Создайте:


# numbers = [1, 2, 3, 4, 5]


# Перемешайте список.

# import random

# raqamho = [1, 2, 3, 4, 5]
# random.shuffle(raqamho)

# print(raqamho)

# ### 32. Перемешать имена

# Создайте список из 10 студентов.

# Перемешайте их.

# import random

# nomhoi_studento = [
#     "Ali", "Bibi", "Farid", "Gulnoza", "Islom",
#     "Madina", "Nodir", "Parvina", "Rustam", "Zarina"
# ]

# random.shuffle(nomhoi_studento)
# print(nomhoi_studento)

# ### 33. Определить порядок участников

# Создайте список участников соревнования.

# Случайно определите порядок выступления с помощью shuffle().

# import random

# ishtirokchiyon = ["Ali", "Bibi", "Farid", "Gulnoza", "Islom"]
# random.shuffle(ishtirokchiyon)

# for navbat, ishtirokchi in enumerate(ishtirokchiyon, start=1):
#     print(navbat, ishtirokchi)

# ### 34. Перемешать вопросы

# Создайте список из 10 вопросов.

# Перемешайте вопросы перед тестом.

# import random

# savolho = [
#     "Poytakhti Tojikiston chi ast?",
#     "2 + 5 chand meshavad?",
#     "Rangi osmon chixeliyay?",
#     "Oftob ay kadom taraf mebroya?",
#     "Soli tavalud?",
#     "Obro кадом ҳайвон менӯшад?",
#     "Китобро дар куҷо мехонанд?",
#     "Забони тоҷикӣ дар куҷо гап зада мешавад?",
#     "Кадом фасл гарм аст?",
#     "Дар як ҳафта чанд рӯз ҳаст?"
# ]

# random.shuffle(savolho)
# print(savolho)

# ### 35. Перемешать карты

# Создайте список:


# ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5"]


# Перемешайте карты.

# import random

# kortho = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5"]
# random.shuffle(kortho)

# print(kortho)

# ### 36. Случайная команда

# Создайте список из 10 студентов.

# Перемешайте список и разделите студентов на 2 команды.

# import random

# donishjuyon = [
#     "Ali", "Bibi", "Farid", "Gulnoza", "Islom",
#     "Madina", "Nodir", "Parvina", "Rustam", "Zarina"
# ]

# random.shuffle(donishjuyon)

# dastai_1 = donishjuyon[:5]
# dastai_2 = donishjuyon[5:]

# print("Dastai 1:", dastai_1)
# print("Dastai 2:", dastai_2)

# ### 37. Разделение на команды

# Создайте 12 участников.

# Случайным образом разделите их на 3 команды по 4 человека.

# import random

# ishtirokchiyon = [
#     "Ali", "Bibi", "Farid", "Gulnoza",
#     "Islom", "Madina", "Nodir", "Parvina",
#     "Rustam", "Zarina", "Komron", "Shabnam"
# ]

# random.shuffle(ishtirokchiyon)

# dastai_1 = ishtirokchiyon[:4]
# dastai_2 = ishtirokchiyon[4:8]
# dastai_3 = ishtirokchiyon[8:12]

# print("Dastai 1:", dastai_1)
# print("Dastai 2:", dastai_2)
# print("Dastai 3:", dastai_3)

# ### 38. Случайный порядок экзамена

# Создайте список студентов.

# Перемешайте список и выведите порядок сдачи экзамена.

# import random

# donishjuyon = ["Ali", "Bibi", "Farid", "Gulnoza", "Islom"]
# random.shuffle(donishjuyon)

# for navbat, donishju in enumerate(donishjuyon, start=1):
#     print(navbat, donishju)

# ### 39. Перемешивание ответов

# Есть 4 варианта ответа на вопрос.

# Перемешайте их перед отображением пользователю.

# import random

# javobho = ["Dushanbe", "Khujand", "Kulob", "Bokhtar"]
# random.shuffle(javobho)

# for javob in javobho:
#     print(javob)

# ### 40. Викторина

# Создайте список вопросов.

# Перемешайте вопросы и проведите небольшую викторину.

# import random

# savolho = [
#     "Poytakhti Tojikiston chi ast?",
#     "2 + 5 chand meshavad?",
#     "Rangi osmon chi ast?"
# ]

# random.shuffle(savolho)

# for savol in savolho:
#     input(savol + " ")

# print("Viktorina tamom shud!")

# # 🟡 Уровень 5 — random.random()

# ### 41. Случайное дробное число

# Сгенерируйте случайное число от 0 до 1.

# import random

# adad = random.random()
# print(adad)

# ### 42. Процент

# Получите случайное число от 0 до 1 и преобразуйте его в процент.

# import random

# foiz = random.random() * 100
# print(foiz, "%")

# ### 43. Шанс 50%

# Создайте программу, которая с вероятностью 50% выводит:


# Успех


# иначе:


# Неудача


# import random

# if random.random() < 0.5:
#     print("Malades")
# else:
#     print("BAxtt omad nakard")

# ### 44. Шанс 30%

# Сделайте событие, которое происходит с вероятностью 30%.

# import random

# if random.random() < 0.3:
#     print("Voqea ruy dod")
# else:
#     print("Voqea ruy nadod")

# ### 45. Шанс 10%

# Создайте событие с вероятностью 10%.

# import random

# event_happened = random.random() < 0.10

# if event_happened:
#     print("Hodisa shid")
# else:
#     print("Hodisa nashid")

# ### 46. Бонус

# Игрок получает бонус с вероятностью 20%.

# Выведите результат:


# Бонус получен!


# или:


# Бонус не получен.

# import random

# bonus = random.random() < 0.20

# if bonus:
#     print('Bonus hast')

# else:
#     print("Bonus nest")




# ### 47. Критический удар

# В игре критический удар происходит с вероятностью 15%.

# Реализуйте механику.

# import random

# bonus = random.random() < 0.15

# if bonus:
#     print('Bonus hast')

# else:
#     print("Bonus nest")

# ### 48. Лотерея

# Создайте систему, где пользователь имеет 5% шанс выиграть.

# import random

# bonus = random.random() < 0.05

# if bonus:
#     print('Bonus hast')

# else:
#     print("Bonus nest")

# ### 49. Случайный подарок

# Пользователь открывает коробку.

# С вероятностью 10% получает подарок.

# import random

# bonus = random.random() < 0.10

# if bonus:
#     print('Bonus hast')

# else:
#     print("Bonus nest")


# ### 50. Монетка 100 раз

# Симулируйте бросок монетки 100 раз.

# Посчитайте:

# * сколько раз выпал орёл;
# * сколько раз выпала решка.

# import random

# diram = 0
# nishon = 0

# for _ in range(100):
#     if random.choice(("орёл", "решка")) == "орёл":
#         diram += 1
#     else:
#         nishon += 1

# print(f"Орёл: {diram}")
# print(f"Решка: {nishon}")



# # 🟡 Уровень 6 — random.choices() и веса

# ### 51. Любимый цвет

# Создайте:


# colors = ["red", "blue", "green"]


# Сделайте вероятности:

# * red — 60%
# * blue — 30%
# * green — 10%

# Используйте random.choices().

# import random

# colors = ["red", "blue", "green"]
# color = random.choices(colors, weights=[60, 30, 10])[0]

# print(color)

# ### 52. Редкость предметов

# Создайте:


# Common
# Rare
# Epic
# Legendary


# Задайте веса:


# 60
# 25
# 10
# 5


# Случайно выдавайте предмет.

# import random

# loot = ["Common", "Rare", "Epic", "Legendary"]
# drop = random.choices(loot, weights=[60, 25, 10, 5])[0]

# print(drop)

# ### 53. Случайная награда

# Создайте систему:


# 10 coins — 50%
# 50 coins — 30%
# 100 coins — 15%
# 1000 coins — 5%

# import random

# rewards = [10, 50, 100, 1000]
# reward = random.choices(rewards, weights=[50, 30, 15, 5])[0]

# print(f"{reward} coins")


# ### 54. Выпадение оружия

# Создайте список:


# Sword
# Bow
# Shield
# Magic Wand


# Задайте разные вероятности выпадения.

# import random

# weapons = ["Sword", "Bow", "Shield", "Magic Wand"]
# weapon = random.choices(
#     weapons,
#     weights=[40, 30, 20, 10]
# )[0]

# print(weapon)

# ### 55. Погода

# Создайте:


# Sunny
# Cloudy
# Rain
# Snow


# Установите разные веса вероятности.

# import random

# weather = ["Sunny", "Cloudy", "Rain", "Snow"]
# today = random.choices(weather, weights=[50, 25, 15, 10])[0]

# print(today)


# ### 56. Генератор ответа

# Создайте ответы:


# Да
# Возможно
# Нет


# Сделайте вероятность:


# Да — 60%
# Возможно — 30%
# Нет — 10%


# import random

# answers = ["Да", "Возможно", "Нет"]
# answer = random.choices(answers, weights=[60, 30, 10])[0]

# print(answer)

# ### 57. Рандомный заказ

# Ресторан получает случайный заказ:


# Pizza
# Burger
# Pasta
# Salad


# У каждого блюда должна быть своя вероятность.

# import random

# food = ["Pizza", "Burger", "Pasta", "Salad"]
# o = random.choices(food, weights=[40, 30, 20, 10])[0]

# print(f"Заказ: {o}")

# ### 58. Система лута

# Создайте систему выпадения:


# Common — 70
# Rare — 20
# Epic — 8
# Legendary — 2


# import random

# loot = ["Common", "Rare", "Epic", "Legendary"]
# drop = random.choices(loot, weights=[70, 20, 8, 2])[0]

# print(f"Выпало: {drop}")

# ### 59. 1000 испытаний

# Запустите систему из задачи №58 1000 раз.

# Посчитайте, сколько раз выпал каждый тип предмета.

# import random
# from collections import Counter

# loot = ["Common", "Rare", "Epic", "Legendary"]
# results = random.choices(loot, weights=[70, 20, 8, 2], k=1000)

# counts = Counter(results)

# for item in loot:
#     print(f"{item}: {counts[item]}")


# ### 60. Сравнение вероятностей

# Создайте систему с весами:


# [70, 20, 10]



# Запустите её 10 000 раз.

# Посмотрите, насколько реальные результаты близки к ожидаемым.

# import random
# from collections import Counter

# items = ["Common", "Rare", "Epic"]
# weights = [70, 20, 10]
# trials = 10_000

# results = random.choices(items, weights=weights, k=trials)
# counts = Counter(results)

# for item, weight in zip(items, weights):
#     expected = trials * weight / sum(weights)
#     actual = counts[item]
#     print(f"{item}: выпало {actual} раз; ожидалось примерно {expected:.0f}")

# # 🟡 Уровень 7 — datetime

# ### 61. Текущая дата

# Выведите сегодняшнюю дату с помощью date.today().

# from datetime import date

# print(date.today())

# ### 62. Текущие дата и время

# Выведите текущие дату и время через datetime.now().

# from datetime import datetime

# print(datetime.now())

# ### 63. Только год

# Получите текущую дату и выведите только год.

# from datetime import date

# today = date.today()
# print(today.year)

# ### 64. Только месяц

# Выведите текущий месяц.

# from datetime import date

# today = date.today()
# print(today.month)

# ### 65. Только день

# Выведите сегодняшний день месяца.
# from datetime import date

# today = date.today()
# print(today.day)

# 66. Текущее время

# Выведите:
# HH:MM:SS

# from datetime import datetime

# current_time = datetime.now()
# print(current_time.strftime("%H:%M:%S"))

# ### 67. Текущая дата

# Выведите:


# DD.MM.YYYY

# from datetime import date

# today = date.today()
# print(today.strftime("%d.%m.%Y"))

# ### 68. Полная дата

# Выведите:


# DD.MM.YYYY HH:MM:SS

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%d.%m.%Y %H:%M:%S"))

# ### 69. Американский формат

# Выведите текущую дату:


# MM/DD/YYYY

# from datetime import date

# today = date.today()
# print(today.strftime("%m/%d/%Y"))

# ### 70. ISO формат

# Выведите текущую дату в формате:


# YYYY-MM-DD

# from datetime import date

# today = date.today()
# print(today.isoformat())

# # 🟠 Уровень 8 — strftime()

# ### 71. Форматирование даты

# Дана дата:
# datetime.now()
# Выведите:
# 29.09.2026

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%d.%m.%Y"))

# ### 72. Форматирование времени

# Выведите:


# 17:30:45

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%H:%M:%S"))

# ### 73. Дата и время

# Выведите:


# 29.09.2026 17:30:45

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%d.%m.%Y %H:%M:%S"))

# ### 74. Год-месяц-день

# Выведите:


# 2026-09-29

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))

# ### 75. День/месяц/год

# Выведите:


# 29/09/2026

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%d/%m/%Y"))

# ### 76. Название дня недели

# Получите текущий день недели через strftime().

# Например:


# Monday

# from datetime import datetime

# today = datetime.now()
# print(today.strftime("%A"))

# ### 77. Название месяца

# Получите название текущего месяца.

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%B"))

# ### 78. Короткий день недели

# Выведите:


# Mon
# Tue
# Wed
# ...

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%a"))

# ### 79. Полное время

# Выведите:


# Hour: 17
# Minute: 30
# Second: 45

# from datetime import datetime

# now = datetime.now()

# print(f"Hour: {now.hour}")
# print(f"Minute: {now.minute}")
# print(f"Second: {now.second}")

# ### 80. Красивый timestamp

# Создайте строку:


# Today is 29.09.2026, time is 17:30:45


# Используйте strftime().

# from datetime import datetime

# now = datetime.now()
# timestamp = now.strftime("Today is %d.%m.%Y, time is %H:%M:%S")
# print(timestamp)

# # 🟠 Уровень 9 — strptime()

# ### 81. Строка в datetime

# Дана:


# "29.09.2026"


# Преобразуйте её в datetime.

# from datetime import datetime

# date_s = "29.09.2026"
# date_o = datetime.strptime(date_s, "%d.%m.%Y")

# print(date_o)

# ### 82. Другая дата

# Преобразуйте:


# 15/05/2025


# в datetime.

# from datetime import datetime

# date_s = "15/05/2025"
# date_o = datetime.strptime(date_s, "%d.%m.%Y")

# print(date_o)

# ### 83. Дата и время

# Преобразуйте:


# 29.09.2026 18:30:00


# в объект datetime.

# ---

# ### 84. ISO строка

# Преобразуйте:


# 2026-09-29


# в datetime.

# from datetime import datetime

# date_s = "2026-09-29"
# date_o = datetime.strptime(date_s, "%Y-%m-%d")

# print(date_o)

# ### 85. Получить год

# Пользователь вводит:


# 15.04.2005


# Преобразуйте строку и получите год рождения.

# from datetime import datetime

# date_s = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
# date_o = datetime.strptime(date_s, "%d.%m.%Y")

# print(date_o.year)

# ### 86. Получить возраст

# Пользователь вводит дату рождения:


# 15.04.2005


# Программа должна определить возраст пользователя.

# from datetime import date, datetime

# date_s = input("Soli tavalud (ДД.ММ.ГГГГ): ")
# date_o = datetime.strptime(date_s, "%d.%m.%Y").date()
# today = date.today()

# age = today.year - date_o.year
# if (today.month, today.day) < (date_o.month, date_o.day):
#     age -= 1

# print(age)

# ### 87. Проверка даты

# Пользователь вводит дату в формате:


# DD.MM.YYYY


# Проверьте, является ли дата корректной.

# from datetime import datetime

# date_s = input("Yagon ruz (DD.MM.YYYY): ")

# try:
#     date_o = datetime.strptime(date_s, "%d.%m.%Y")
#     print("Tugriyay")
# except ValueError:
#     print("Hatohay")

# ### 88. Изменение формата

# Пользователь вводит:


# 29.09.2026


# Программа должна вывести:


# 2026-09-29

# from datetime import datetime

# date_s = input("Yagon ruz (DD.MM.YYYY): ")
# date_o = datetime.strptime(date_s, "%d.%m.%Y")

# print(date_o.strftime("%Y-%m-%d"))

# ### 89. Два формата

# Пользователь вводит дату:


# 29.09.2026


# Выведите её в двух форматах:


# 29/09/2026
# 2026-09-29

# from datetime import datetime

# date_s = input("Введите дату (DD.MM.YYYY): ")
# date_o = datetime.strptime(date_s, "%d.%m.%Y")

# print(date_o.strftime("%d/%m/%Y"))
# print(date_o.strftime("%Y-%m-%d"))

# ### 90. Дата регистрации

# Пользователь вводит:


# 25.09.2026 14:30


# Преобразуйте строку в datetime.

# Затем выведите:


# Registration date: 25.09.2026
# Registration time: 14:30

# from datetime import datetime

# date_s = input("Ruz sol (DD.MM.YYYY HH:MM): ")
# date_o = datetime.strptime(date_s, "%d.%m.%Y %H:%M")

# print(f"Registration date: {date_o.strftime('%d.%m.%Y')}")
# print(f"Registration time: {date_o.strftime('%H:%M')}")

# # 🔴 Уровень 10 — Смешанные задачи

# ### 91. Генератор OTP

# Создайте программу, которая:

# 1. генерирует случайный 6-значный код;
# 2. показывает код;
# 3. ждёт 5 секунд;
# 4. сообщает:


# Code expired!


# Используйте:

# * random
# * time

# import random
# import time

# code = random.randint(100_000, 999_999)
# print(code)

# time.sleep(5)
# print("Code expired!")


# ### 92. Игра на скорость

# Программа выводит:


# Get ready...


# Через случайное количество секунд от 1 до 5 выводит:


# GO!


# Пользователь должен как можно быстрее нажать Enter.

# Измерьте его время.

# ---

# ### 93. Таймер реакции

# Компьютер случайно ждёт от 2 до 5 секунд.

# После этого выводит:


# PRESS ENTER!


# Измерьте время реакции пользователя.

# ---

# ### 94. Случайный студент + время

# Создайте список студентов.

# Программа:

# 1. случайно выбирает студента;
# 2. показывает его имя;
# 3. ждёт 3 секунды;
# 4. выводит:


# Answer now!


# ---

# ### 95. Викторина

# Создайте минимум 5 вопросов.

# Программа должна:

# 1. перемешать вопросы;
# 2. задавать их пользователю;
# 3. считать правильные ответы;
# 4. в конце показать время прохождения теста.

# Используйте:

# * random.shuffle()
# * time.time()

# ---

# ### 96. Лотерея

# Создайте лотерею.

# Участник получает один из призов:


# 100 сомони
# 50 сомони
# 20 сомони
# Ничего


# У каждого результата должна быть своя вероятность.

# После выбора покажите текущее время выигрыша через:


# datetime.now()


# ---

# ### 97. Система регистрации

# Пользователь вводит:


# Имя
# Дата рождения


# Например:


# Ali
# 15.04.2005


# Программа должна:

# 1. преобразовать дату через strptime();
# 2. определить возраст;
# 3. получить текущую дату;
# 4. вывести информацию через strftime().

# ---

### 98. Система заказов

# Создайте программу, которая случайно выбирает товар:


# Laptop
# Phone
# Keyboard
# Mouse
# Monitor


# Для каждого товара задайте свою вероятность.

# После выбора создайте:


# Order created at: DD.MM.YYYY HH:MM:SS


# ---

# ### 99. Мини-игра "Казино"

# Создайте игру.

# Игрок начинает с:


# 100 coins


# Каждый раунд:

# 1. игрок делает ставку;
# 2. компьютер случайно выбирает результат;
# 3. используются разные вероятности выигрыша;
# 4. баланс изменяется;
# 5. показывается время раунда.

# Игра заканчивается, если:

# * баланс равен 0;
# * пользователь выходит из игры.

# Используйте:

# * random
# * random.choices()
# * datetime
# * strftime()

# ---

# ### 100. Финальный проект — Random Quiz System

# Создайте полноценную консольную систему тестирования.

# ## Требования

# У пользователя есть список вопросов.

# Каждый вопрос содержит:

# * текст;
# * варианты ответов;
# * правильный ответ.

# Программа должна:

# ### 1. Начать тест

# Показать:


# ===== QUIZ =====


# ---

# ### 2. Засечь время

# Запомнить время начала:


# time.time()


# ---

# ### 3. Перемешать вопросы

# Использовать:


# random.shuffle()


# ---

# ### 4. Перемешать ответы

# Варианты ответов каждого вопроса также должны перемешиваться.

# ---

# ### 5. Задавать вопросы

# Пользователь отвечает на каждый вопрос.

# ---

# ### 6. Подсчитывать результат

# Например:


# Correct: 8
# Wrong: 2


# ---

# ### 7. Рассчитать процент

# Например:


# Score: 80%


# ---

# ### 8. Засечь время окончания

# Использовать:


# time.time()


# и определить продолжительность теста.

# ---

# ### 9. Показать дату

# Использовать:


# datetime.now()


# и:


# strftime()


# Результат:


# Test date: 29.09.2026
# Test time: 17:45:32


# ---

# ### 10. Показать итог

# Например:


# ========================
#         RESULT
# ========================

# Correct: 8
# Wrong: 2
# Score: 80%

# Time: 42.5 seconds

# Date: 29.09.2026
# Time: 17:45:32

# ========================


# ---