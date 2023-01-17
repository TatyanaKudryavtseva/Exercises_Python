# Нам необходимо рассчитать площадь геометрической фигуры на основе полиморфизма:
import math
class NonPositiveDigitException(ValueError):
    pass

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self): # Для решения используем специальный метод get_area. Он принимает аргумент self,
        # то есть сам класс Rectangle, и возвращает произведение атрибута a (ширина) на b (высота).
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2 # возведение в степень **2 (в квадрат)

class Circle:
    def __init__(self, r):
        if r <= 0:
            raise NonPositiveDigitException("The circle's radius can't take negative values or 0")
        self.r = r
    def get_area_circle(self):
        return math.pi * self.r ** 2
