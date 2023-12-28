print(f'I am {__name__}')


import sys
print(sys.path)

# import other

def a1_func():
    print("Выполняем a1_func()")

# Абсолютные импорты:
# import other
# import packA.a2
# import packA.subA.sa1

# Явные относительные импорты:
# import other
# from . import a2
# from .subA import sa1

# Неявные относительные импорты (не поддерживаются в Python 3):
# import other
# import a2
# import subA.sa1


