# опыт 1

file = open("inform_file.txt", "r", encoding="utf-16le")
line = file.read()
print(line)

# опыт 2

with open("file_.txt", "w") as file:
    file.write("qwerty")
with open("file_.txt", "r") as file:
    line = file.readlines()
    print(line)

# опыт 3

students = [
    {"name": "John", "age": 23},
    {"name": "Jane", "age": 22},
    {"name": "Mike", "age": 24},
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(f"Name: {student['name']}, Age: {student['age']}\n")

with open("students.txt", "r", encoding="windows-1251") as file:
    print(file.readlines())

# задача 1
with open("log.txt", "w", encoding="utf-8") as file:
    file.write(r"Log Entry 1\n")
with open("log.txt", "r", encoding="utf-8") as file:
    print(file.read())
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Log Entry 2")
with open("log.txt", "r", encoding="utf-8") as file:
    print(file.read())

# задача 2

with open("shopping_list.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("bread\n")
    file.write("tomatoes\n")
with open("shopping_list.txt", "r", encoding="utf-8") as file:
    print(file.read())
with open("shopping_list.txt", "a", encoding="utf-8") as file:
    file.write("cheese\n")
    file.write("eggs")
with open("shopping_list.txt", "r", encoding="utf-8") as file:
    print(file.read())
