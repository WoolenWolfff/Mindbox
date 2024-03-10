# -*- coding: utf-8 -*-
"""
Модуль, позволяющий легко найти площадь круга, треугольника, квадрата и прямоугольника.
Длины сторон следует задавать через пробел.
"""

import numpy as np

def S():
  flag = True
  while flag:
    sides = list(map(int, input('Радиус или длины сторон ').split()))

    # Круг
    if len(sides) == 1:
      s = np.pi * sides[0] ** 2
      print('Площадь круга: {:.2f}'.format(s))
      flag = False

    # Квадрат/прямоугольник
    elif len(sides) == 2:
      s = sides[0] * sides[1]
      flag = False
      if sides[0] == sides[1]:
        print('Площадь квадрата: {:.2f}'.format(s))
      else:
        print('Площадь прямоугольника: {:.2f}'.format(s))

    # Треугольник
    elif len(sides) == 3:
      flag = False
      if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] \
      and sides[0] + sides[2] > sides[1]:
        sides = np.sort(sides)
        if np.sqrt(sides[0] ** 2 + sides[1] ** 2) == sides[2]:
          s = sides[0] * sides[1] / 2.
          print('Треугольник прямоугольный.\nПлощадь: {:.2f}'.format(s))
        else:
          p = np.sum(sides) / 2.
          s = np.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
          print('Треугольник непрямоугольный.\nПлощадь: {:.2f}'.format(s))
      else:
        print('Треугольник с такими сторонами не существует.')
      
    else:
      print('Непредусмотренное количество сторон.')