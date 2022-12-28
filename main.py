# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts
def attack(char_name: str, char_class: str) -> str:
    """Описывает работу функции attack."""
    ...


def defence(char_name: str, char_class: str) -> str:
    """Описывает работу функции defence."""
    ...


def special(char_name: str, char_class: str) -> str:
    """Описывает работу функции special."""
    ...


def start_training(char_name: str, char_class: str) -> str:
    """Описывает работу функции start_training."""
    ...


def choice_char_class() -> str:
    """Описывает работу функции choice_char_class."""
    ...


def main() -> None:
    """Описывает работу функции при старте игры."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
