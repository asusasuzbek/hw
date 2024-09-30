# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:21:37 2024

@author: Компьютер
"""
import math pi, cos
print("Введите длину первой стороны: ")
a = input()
print("Введите длину второй стороны: ")
b = input()
print("Введите угол между ними в градусах: ")
angle = input()

a = float(a)
b = float(b)
angle = float(angle)

angle_radians = math.radians(angle) 

c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_radians))

print("Длина третьей стороны: ", c)
