# SECTION 1: DECORATORS
print("=" * 60)
print("SECTION 1: DECORATORS")
print("=" * 60)

def my_decorator(func):
    def wrapper():
        print("İlk İşlem")
        func()
        print("İkinci İşlem")

    return wrapper

@my_decorator
def hello_world():
    print("Hello World!")

hello_world()


# SECTION 2: PROPERTY DECORATORS

print("=" * 60)
print("SECTION 2: PROPERTY DECORATORS")
print("=" * 60)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property           # Burası getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) <= 0:
            raise ValueError("Name must be longer")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be a integer")
        if value < 0:
            raise ValueError("Age must be positive")
        self.__age = value

person1 = Person("Ali İhsan", 22)
print("First Name " + person1.name)
person1.name = "Ali İhsan Sancar"
print("Second Name " + person1.name)
print("First Age " + str(person1.age))
person1.age = 36
print("Second Age " + str(person1.age))


# SECTION 3: STATIC METHOD

print("=" * 60)
print("SECTION 3: STATIC METHODS")
print("=" * 60)

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
# Statik Methodların amacı mainde kullanırken bir instance oluşturmaya gerek kalmaması
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Denominator can not be 0")
        return x / y

print(MathOperations.add(3,6))
print(MathOperations.divide(3,6))


# SECTION 4: CLASS METHOD

print("=" * 60)
print("SECTION 4: CLASS METHODS")
print("=" * 60)

class Pizza:

    total_pizzas = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.total_pizzas += 1

    @classmethod
    def karisik(cls):
        return cls(['Mısır', 'Sucuk', 'Peynir', 'Domates'])

    @classmethod
    def vegan(cls):
        return cls(['Kasar', 'Feslegen', 'Domates'])

    @classmethod
    def patatesli(cls):
        return cls(['Patates', 'Domates'])

    @classmethod
    def get_total_pizzas(cls):
        return cls.total_pizzas

pizza1 = Pizza.karisik()
print(pizza1.ingredients)

pizza2 = Pizza.vegan()
print(pizza2.ingredients)

pizza3 = Pizza.patatesli()
print(pizza3.ingredients)

print(Pizza.get_total_pizzas())


# SECTION 5: ABSTRACT METHODS

print("=" * 60)
print("SECTION 5: ABSTRACT METHODS")
print("=" * 60)

from abc import abstractmethod
class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Hav hav")

    def move(self):
        print("Köpek yürüdü")

    def sleep(self):
        print("Kopek uyudu")


hayvan = Dog("karabaş")
print(hayvan.name)
hayvan.move()


# SECTION 6: OVERLOADING

print("=" * 60)
print("SECTION 6: OVERLOADING")
print("=" * 60)

from typing import overload, Union

class Calculator:
    @overload
    def add(self, a: int, b: int)->int:
        ...

    @overload
    def add(self, a: int, b: int, c: int)->int:
        ...

    # Bunların başına overload yazmak bir şey fark etmeyecek sadece tanımlama yapmış olacağız daha düzgün bir kod yazımı için
    # Sorunun çözümü için aşağıdaki gibi yazmamız gerkiyor

    def add(self, a: int, b: int, c: int | None = None) -> int:     # 3. parametre ya int olacak ya da None olacak yani olmayacak ve değeri default olarak boş olacak
        if c is None:
            return a + b
        return a + b + c

    @overload
    def process(self, value: int) -> int:
        ...

    @overload
    def process(self, value: str) -> str:
        ...

    def process(self, value: Union[int, str]) -> Union[int, str]:
        if isinstance(value, int):
            return value * 2
        elif isinstance(value, str):
            return value.upper()
        else:
            raise ValueError("Value must be a integer or string")

calculator = Calculator()
print(calculator.add(10,20))
print(calculator.add(10,20,30))
print(calculator.process(20))
print(calculator.process("alihsancar"))


# ============================================================================
# SECTION 7: FINAL CLASSES AND METHODS (@final)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 7: FINAL DECORATOR")
print("=" * 60)

from typing import final

class BaseGame:
    def start(self):
        print("Game is starting")

    @final
    def calculate_score(self, points: int) -> int:
        bonus = 100
        return points + bonus

    def end(self):
        print("Game over")

class MyGame(BaseGame):
    def start(self):
        print("My Game starting with custom intro")

@final
class SecretAlgorithm:
    def process(self):
        print("Processing secret algorithm")

print("\nExample 12: Final Methods")
game = MyGame()
game.start()
score = game.calculate_score(50)
print(f"  Final score: {score}")
game.end()

print("\nExample 13: Final Class")
secret = SecretAlgorithm()
secret.process()

'''
# ============================================================================
# SECTION 8: OVERRIDE DECORATOR (@override)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 8: OVERRIDE DECORATOR")
print("=" * 60)



from typing import override


class Shape:
    def area(self):
        return 0.0

    def perimeter(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @override
    def area(self):
        return self.weight * self.height

    @override
    def perimeter(self):
        return (self.weight + self.height) * 2

rect = Rectangle(5,3)
print(rect.area())
print(rect.perimeter())
'''
# ============================================================================
# BONUS SECTION: COMBINING DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("BONUS: COMBINING MULTIPLE DECORATORS")
print("=" * 60)

def multiply_decorator(func):
    def wrapper(x :int):
        return func(x) * 2
    return wrapper

def other_decorator(func):
    def wrapper(x: int):
        return func(x) * 4
    return wrapper

@other_decorator
@multiply_decorator
def calculate(x: int):
    return x * 2

print(calculate(10))