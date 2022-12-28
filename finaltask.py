from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для '
                'вычисления квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: str):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Выполняет условие если меньше или равно нулю."""
    if your_number <= 0:
        return
    more = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из '
          f'введённого вами числа. '
          f'Это будет {more}')


calc(25.5)
