class Animal:
    """Класс животных"""
    def __init__(self, name: str, weight: float, age: int, habitat: str):
        """
        Параметры:
        name: str - название животного
        weight: float - вес животного в килограммах
        age: int - возраст животного в полных годах
        habitat: str - место нахождения животного
        """
        self.name = name
        self.weight = weight
        self.age = age
        self.habitat = habitat

    def is_heavy(self) -> bool:
        """
        Проверяется, тяжелее ли животное среднего веса среди всех животных
        """
        ...

    def habitat_change(self, new_habitat) -> str:
        """
        Животное сменило место своего пребывания
        """
        ...

    def __str__(self):
        return f"Название животного {self.name}. Вес животного {self.weight}. Возраст животного {self.age}. Место нахождения животного {self.habitat}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r}, age={self.age!r}, habitat={self.habitat!r})"



class Bird(Animal):
    """Класс птиц"""
    def __init__(self, name: str, weight: float, age: int, habitat: str, wingspan: float, range_of_flight: float):
        """
        Параметры:
        name: str - название животного
        weight: float - вес животного в килограммах
        age: int - возраст животного в полных годах
        habitat: str - место нахождения животного
        wingspan: float - размах крыльев в сантиметрах
        range_of_flight: float - максимальная дальность перелёта в километрах
        """
        super().__init__(name=name, weight=weight, age=age, habitat=habitat)
        self.wingspan = wingspan
        self.range_of_flight = range_of_flight

    def is_heavy(self) -> bool:
        """
        Проверяется, тяжелее ли птица среднего веса среди всех птиц

        Данный метод должен быть перегружен, т.к. в данный момент нас интересует средняя масса птиц, а не животных вообще. Константа сравнения другая должна быть.
        """
        ...

    def habitat_change(self, new_habitat) -> str:
        """
        Птица сменила место своего пребывания
        """
        super().habitat_change(new_habitat=new_habitat)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r}, age={self.age!r}, habitat={self.habitat!r}, wingspan={self.wingspan!r}, range_of_flight={self.range_of_flight!r})"