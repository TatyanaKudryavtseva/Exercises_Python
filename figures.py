from figures_classes import Rectangle, Square, Circle
# далее создаём два прямоукольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
print(rect_1.get_area())
print(rect_2.get_area())
# Добавим в нашу программу еще один объект, например Square (квадрат), который принимает в качестве аргумента
# одну сторону. Добавляем данные в исходный файл rectangle.py:

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), square_2.get_area_square())
# Теперь мы хотим в нашей программе все объекты перенести в единую коллекцию. Назовем фигуры (figures).
# Коллекция содержит список, в который мы помещаем наш первый прямоугольник, квадрат и т.д. (см 17 строчку)

# Это необходимо, чтобы найти площадь каждой фигуры, сохраненной в списке figures. Обратите внимание,
# мы будем работать с прямоугольниками и квадратами с помощью одинаковых методов: get_area(). Внутри цикла проверяем:
# Если экземпляр класса figure является квадратом, то вызываем метод get_area().
# В противном случае — обрабатываем данные для прямоугольника методом get_area().
# В условии есть функция isinstance, поддерживающая наследование. Она проверяет, является ли аргумент объекта
# экземпляром класса или экземпляром класса из кортежа. В случае если является, функция возвращает True,
# если не является — False.

# Добавьте еще один класс — круг (class Circle), который принимает в качестве аргументов свой радиус.

circle_1 = Circle(2)
circle_2 = Circle(3)

print(circle_1.get_area_circle(), circle_2.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
# Далее пройдемся по циклу for:
for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_area())
    elif isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area_circle())
