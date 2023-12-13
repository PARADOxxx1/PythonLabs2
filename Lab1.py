import doctest

class Vector:
    def __init__(self, x: float, y: float):
        """
        Создание и подготовка к работе объекта "Вектор"

        :param x: Координата по оси ox
        :param y: Координата по оси oy

        Примеры:
        >>> vector = Vector(15, 10)
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Координата только типа int или float')
        self.x = x
        self.y = y

    def multiply(self, a: float) -> None:
        """
        Умножение вектора на число
        :param a: Число, на которое умножается вектор

        Примеры:
        >>> vector = Vector(15, 10)
        >>> vector.multiply(2)
        """
        ...

    def length(self) -> float:
        """
        Вычисление длины вектора

        :return: длина вектора

        Примеры:
        >>> vector = Vector(15, 10)
        >>> vector.length()
        """
        ...


class Ellipse:
    def __init__(self, a: float, b: float):
        """
        Создание и подготовка к работе объекта "Эллипс"

        :param a: Первая полуось эллипса
        :param b: Вторая полуось эллипса

        Примеры:
        >>> ellipse = Ellipse(10, 5)
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Полуось только типа int или float')
        if a <= 0 or b <= 0:
            raise TypeError('Полуось принимает только положительные значения')
        self.a = a
        self.b = b

    def square(self) -> float:
        """
        Вычисление площади эллипса

        :return: Площадь эллипса

        Примеры:
        >>> ellipse = Ellipse(10, 5)
        >>> ellipse.square()
        """
        ...

    def length(self) -> float:
        """
        Вычисление длины окружности эллипса

        :return: Длина окружности эллипса

        Примеры:
        >>> ellipse = Ellipse(10, 5)
        >>> ellipse.length()
        """
        ...


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param a: Первая сторона треугольника
        :param b: Вторая сторона треугольника
        :param c: Третья сторона треугольника

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Сторона треугольника только типа int или float')
        if a <= 0 or b <= 0 or c <= 0:
            raise TypeError('Стороны треугольника строго положительны')
        if a >= b + c or b >= a + c or c >= a + b:
            raise TypeError('Треугольник не существует, не выполняется неравенство треугольника')
        self.a = a
        self.b = b
        self.c = c

    def is_triangle_right(self) -> bool:
        """
        Проверка, является ли треугольник прямоугольным

        :return: Является ли треугольник прямоугольным

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        >>> triangle.is_triangle_right()
        """
        ...

    def is_triangle_equilateral(self) -> bool:
        """
        Проверка, является ли треугольник равносторонним

        :return: Является ли треугольник равносторонним

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        >>> triangle.is_triangle_equilateral()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()