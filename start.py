print(f'I am {__name__}')

# import math
# import random

# import sys
# print(sys.path)

# import pkgutil
# search_path = ['.']  # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)

import packA.a1


import packA  # «import packA.a1» сработает точно так же

packA.packA_func()
packA.a1_func()
packA.a1.a1_func()

# вар 1
# from packA.subA.sa1 import helloWorld
# helloWorld()

# вар 2
# from packA.subA import sa1 # или то же самое
# import packA.subA.sa1 as sa1
# sa1.helloWorld()

# вар 3
# import packA.subA.sa1
# packA.subA.sa1.helloWorld()
