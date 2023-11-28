import logging


logger = logging.getLogger('calculator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Создаем абстрактный класс Operation, который будет представлять операцию калькулятора
class Operation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # Абстрактный метод execute, который будет возвращать результат операции
    def execute(self):
        raise NotImplementedError

# Создаем класс Addition, который наследуется от Operation и реализует операцию сложения
class Addition(Operation):
    def execute(self):
        return self.left + self.right

# Создаем класс Multiplication, который наследуется от Operation и реализует операцию умножения
class Multiplication(Operation):
    def execute(self):
        return self.left * self.right

# Создаем класс Division, который наследуется от Operation и реализует операцию деления
class Division(Operation):
    def execute(self):
        if self.right != 0:
            return self.left / self.right
        else:
            return None

# Создаем класс Calculator, который будет выполнять операции над вещественными числами
class Calculator:
    def __init__(self, operation):
        self.operation = operation

    # Метод calculate вызывает метод execute у объекта operation и возвращает его результат
    def calculate(self):
        result = self.operation.execute()
        # Логируем операцию и результат
        logger.debug(f'Выполнена операция {self.operation.__class__.__name__} над {self.operation.left} и {self.operation.right}, результат: {result}')
        return result


# Создаем объекты класса Calculator с разными операциями
calc_add = Calculator(Addition(3.5, 2.7))
calc_mul = Calculator(Multiplication(4.2, 5.1))
calc_div = Calculator(Division(9.6, 3.2))

# Вызываем метод calculate у каждого объекта Calculator и выводим результат в консоль
print(calc_add.calculate())
print(calc_mul.calculate())
print(calc_div.calculate())