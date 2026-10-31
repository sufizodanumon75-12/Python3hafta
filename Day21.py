# file = open('file.txt','r')
# print(file.read())

# file = open('file.txt','w')
# file.write(' Hello')

# file = open('file.txt','a')
# file.write(' Hello')

# file.close()

# file.read()
# try:
#     file = open('file.txt','r')
#     print(file.read())
# except:
#     print('Not Found')
# finally:
#     file.close()

# with open('file.txt') as file:
#     print(file.read())

# with open('file.txt','r') as file:
#     lines = file.readline()
#     print(lines)




# ---------------------------------Homework---------------------------------------------
# 1\. Создание файла

# Напишите программу, которая создаёт файл text.txt и записывает в него 5 строк текста. Каждая строка должна содержать отдельное предложение.

# salom = [
#     "Hello world",
#     "Good night",
#     "Good evening",
#     "Good morning",
#     "Welcome to Tajikistan"
# ]

# with open("file.txt", "w", ) as file:
#     file.write("\n".join(salom) + "\n")

# 2\. Чтение файла

# Создайте программу, которая читает файл text.txt и выводит всё его содержимое в консоль.

# with open("file.txt", "r",) as file:
#     print(file.read())

# 3\. Подсчёт строк

# Дан текстовый файл text.txt. Посчитайте, сколько строк содержится в файле.

# with open("file.txt", "r") as file:
#     lines = file.readlines()

# print("Chan kadaray: ", len(lines))

# 4\. Подсчёт слов

# Напишите программу, которая читает текстовый файл и определяет общее количество слов в нём.

# with open("file.txt", "r") as file:
#     text = file.read()

# print("Chand kalimahay:", len(text.split()))

# 5\. Подсчёт символов

# Дан файл text.txt. Найдите количество символов в файле, не учитывая пробелы и символы переноса строки.

# with open("file.txt", "r") as file:
#     text = file.read()

# count = sum(not char.isspace() for char in text)
# print("Chad simvol dora: ", count)

# 6\. Поиск слова

# Пользователь вводит слово. Программа должна найти, сколько раз это слово встречается в текстовом файле.



# 7\. Копирование содержимого

# Дан файл source.txt. Создайте файл copy.txt и скопируйте в него всё содержимое первого файла.

# sentence = input("Gumlara navis: ")

# with open("file.txt", "a") as file:
#     file.write(sentence + "\n")

# 8\. Добавление текста

# Напишите программу, которая запрашивает у пользователя предложение и добавляет его в конец файла text.txt, не удаляя старое содержимое.



# 9\. Поиск самой длинной строки

# Дан текстовый файл. Найдите и выведите самую длинную строку, а также количество символов в ней.

# 10\. Анализ текста

# Дан текстовый файл text.txt. Программа должна:

# * Посчитать количество строк.

# * Посчитать количество слов.

# * Посчитать количество символов.

# * Найти самое длинное слово.

# * Найти самое короткое слово.

# * Вывести 5 наиболее часто встречающихся слов.