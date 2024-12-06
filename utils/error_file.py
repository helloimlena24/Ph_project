# #исправляем ошибку File Error - переносим файл в текущую директорию
# with open("file_1.txt", 'r', encoding="utf-8") as file:
#     print(file.read())
#
#
# #исправляем ошибку File Error - указываем абс. путь от С, при это файл в тек.дир:
import os

# way_file = os.path.join(r"C:\Ph_Project\utils", "file_1.txt")
# with open(way_file, 'r', encoding="utf-8") as file:
#     print(file.read())

# исправляем ошибку File Error - указываем абс. путь от С, при это файл НЕ в тек.дир, а в др. директории:
# bath_way = r"C:\Ph_Project"

bath_way = os.path.dirname(__file__)
# чтобы работало на всех ПК - пишем в bath_way "os.path.dirname(__file__)"
# txt_way = r"other_direct\file_2.txt"
full_way = os.path.join(bath_way, "other_direct", "file_2.txt")
with open(full_way, "r", encoding="utf-8") as file:
    print(file.read())

# #относительный путь
# with open(r"other_direct\file_2.txt", 'r', encoding="utf-8") as file:
#     print(file.read())
