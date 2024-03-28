import os
import sys


def add_new_user(name: str, phone: str, filename: str):
   """
   Добавление нового пользователя.
   """
   new_line = '\n' if read_all(filename) != "" else ''
   with open(filename, "a", encoding="utf-8") as file:
      file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
   """
   Возвращает все содержимое телефонной книги.
   """
   with open(filename, "r", encoding="utf-8") as file:
      return file.read()


def search_user(filename: str, data: str) -> str:
   """
   Поиск записи по критерию data.
   """
   with open(filename, "r", encoding="utf-8") as file:
      list_1 = file.read().split("\n")
   result = [i for i in list_1 if data in i]
   if not result:
      return "По указанному значению совпадений не найдено"
   return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
   """
   Функция для переноса указанной строки из одного файла
   в другой
   source: str - имя исходного файла
   dest: str - имя файла куда переносим
   num_row: int - номер переносимой строки
   """
   list_1 = read_all(source).split("\n")
   list_2 = read_all(dest).split("\n")
   if len(list_1) < num_row:
      print("Ошибка! Запись с таким номером не обнаружена")
   else:
      for i in range(len(list_1)):
         if num_row-1 == i:
            result = list_1[i]
      if result not in list_2:
         result = result.split(' - ')
         add_new_user(result[0], result[1], dest)
      else:
         print("Такой человек с таким же номером уже существует в списке")   


INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file = "text.txt"
file2 = "text2.txt"

if file not in os.listdir():
   print("указанное имя файла отсутсвует")
   sys.exit()


while True:
   mode = int(input(INFO_STRING))
   if mode == 1:
      print(read_all(file))
   elif mode == 2:
      name = input("Введите Ваше имя: ")
      phone = input("Введите Ваш телефон: ")
      add_new_user(name, phone, file)
   elif mode == 3:
      data = input("Введите значение: ")
      print(search_user(file, data))
   elif mode == 4:
      num_row = int(input('Введите номер копируемой строки: '))
      transfer_data(file, file2, num_row)