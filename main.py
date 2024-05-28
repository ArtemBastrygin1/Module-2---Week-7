import random
import string
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)


class TreasureMap:
    def __init__(self, size=10):
        self.size = size
        # местоположение_сокровища = генерация местоположения сокровища
        self.treasure_location = self.generate_treasure_location()
        # grid = сетка
        self.grid = [['~' for _ in range(size)] for _ in range(size)]

    def generate_treasure_location(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        logging.info(f'Координаты {x}, {y}')
        return (x, y)

    # проверка на наличие сокровища
    def is_treasure_at(self, x, y):
        return (x, y) == self.treasure_location

    # получить подсказку
    def get_hint(self, x, y):
        treasure_x, treasure_y = self.treasure_location
        distance = abs(treasure_x - x) + abs(treasure_y - y)
        if distance == 0:
            return 'Поздравляем! Вы выиграли сокровище!'
        elif distance <= 2:
            return 'Вы очень близко к сокровищу!'
        elif distance <= 5:
            return 'Вы близко к сокровищу!'
        else:
            return 'Вы далеко от сокровища!'

    # отображение
    def display(self):
        # row - ряд
        for row in self.grid:
            print(' '.join(row))


class Player:
    def __init__(self, name):
        self.name = name
        # догадки
        self.guesses = []
        # attempts - попытки
        self.attempts = 0

    def make_guess(self, guess):
        x, y = guess
        self.guesses.append((x, y))
        self.attempts += 1
        return x, y


class Game:
    def __init__(self, player, treasure_map):
        self.player = player
        self.treasure_map = treasure_map

    def play(self):
        print('Добро пожаловать в игру «Поиск сокровища»!')
        print('На игровом поле размером 10x10 спрятано сокровище.')
        print('Ваша задача — найти его за минимальное количество попыток.')
        print('Координаты вводятся в формате «x, y», где x — горизонтальная координата, y — вертикальная координата.')
        print('Удачи!')

        while True:
            self.treasure_map.display()
            guess = input(
                'Введите координаты, чтобы проверить, '
                'содержится ли сокровище в этой клетке (например 3, а): '
            )

            try:
                x, y = guess.split(',')
                x = int(x.strip())
                y = string.ascii_lowercase.index(y.strip())
            except ValueError:
                print('"Ошибка! Введите координаты в формате «x, y». Например: 3, а.')
                continue
            logging.info(f'{self.player.name}. Предполагаемые координаты ({x}, {y})')
            x, y = self.player.make_guess((x, y))

            if self.treasure_map.is_treasure_at(x, y):
                print("Поздравляем! Вы нашли сокровище.")
                print(f"Игра завершена. Сокровище найдено. Попыток: {self.player.attempts}.")
                print("Ваш промокод SUPER100")
                logging.info(
                    f"{self.player.name} нашел сокровище за {self.player.attempts} попыток."
                )
                break

            else:
                hint = self.treasure_map.get_hint(x, y)
                print(hint)
                logging.info(hint)

            if self.player.attempts >= 20:
                print("Количество попыток исчерпано. Сокровище не найдено.")
                logging.info("Игра закончена. Достигнуто максимальное количество попыток.")
                break


# #print('Предыгровая настройка')
# player_name = input('Введите ваше имя: ')
# player = Player(player_name)
# treasure_map = TreasureMap()
# game = Game(player, treasure_map)
# game.play()


