import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):# определяем подготовительный метод setup, в котором будем создавать объект калькулятора
    # из импортируемого класса
        self.calc = Calculator
    # Далее можно писать тесты. Они тоже начинаются со слова test т.к Pytest по названию определяет что ему спользовать
    # для тестов

    def test_multiply_calculate_correctly(self):# в названии обязательно пишем ф-ию, кот. мы определяем и результат
        # который она должна вернуть, кот. мы ожидаем
        assert self.calc.multiply(self, 2, 2) == 4# с помощью assert мы сравниваем ожидание с результатом
    # Добавим отрицательный тест, который будет валиться у нас

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding (self, 5, 2) == 7