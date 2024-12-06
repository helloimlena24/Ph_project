# абсолютный импорт
from utils.example import calculation

print(calculation(1, 2))

from utils import example

print(example.calculation(1, 3))

from utils.example import *

print(calculation(1, 5))

# относительный импорт
# from .import example
# print(example.calculation(1, 4))

# from .example import calculation
# print(calculation(5, 6))
#
# from .utils.example import calculation
# print(calculation(1, 4))
