import os

print(
    os.getcwd(),
    os.listdir(),
)

import os

path1 = r"/path/to/directory"
path2 = "file.txt"

joined_path = os.path.join(path1, path2)
print(joined_path)


print(os.path.dirname(joined_path))

# В нашей программе или в интерпретаторе Python вы можете выяснить,
# какая у вас текущая рабочая директория, используя следующий код:
import os

current_directory = os.getcwd()
print(current_directory)

current_directory = os.getcwd()
print(os.listdir(current_directory))
