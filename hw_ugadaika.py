# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import random

a = random.randint(0,99)


while True:
    try:
        print("Угадай число от 0 до 99: ")
        b = input() 
        b = int(b)
        
        if b < 0 or b > 99:
            print("Число должно быть от 0 до 99")
            continue 
        if a == b:
            print("Вы угадали!")
            break
        elif a < b:
            print("Вы не угадали. Число должно быть меньше")
        else:
            print("Вы не угадали. Число должно быть больше")
    except:
        print("Ошибка")