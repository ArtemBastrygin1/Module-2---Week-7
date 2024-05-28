# Поиск сокровища

## Описание
Этот код представляет собой консольную игру
"Поиск сокровища". Игроку предлагается найти
сокровище на игровом поле размеров 10x10, вводя
координаты клетки, в которой, по его мнению, может
находиться сокровище. После каждого хода игрок получает
подсказку о том, насколько близко он находится к 
сокровищу.

## Как играть
- Запустите файл `main.py`
- Введите свое имя.
- Следуйте инструкциям на экране, вводя координаты клеток в формате "x, y". Где `x` - горизонтальная координата (число от 0 до 9), `y` - вертикальная координата (буква от a до j)

## Функциональность
- В игре используется логирование действий игрока и системы в файл `log.txt`.
- Используется манхэттенское расстояние для подсчета расстояния между клетками.
- Игра предоставляет подсказки о близости к сокровищу.
- Максимальное количество попыток ограничено 20.

## Пример сообщений в логах
- `2024-05-27 12:00:00 - INFO - Player. Предполагаемые координаты (5, 3)`
- `2024-05-27 12:00:15 - INFO - Вы далеко от сокровища!`
- `2024-05-27 12:00: 45 - INFO - Player нашел сокровище за 4 попыток.`

## Примечание

- Убедитесь, что ваш файл `log.txt` создан в той же директории где
находится `main.py`
- В функции `generate_treasure_location` строку `#logging.info(f'Координаты {x}, {y}')` можно либо удалить, либо оставить под комментарием. Эта строка используется для вывода координат, которые были загаданы, и может быть полезна для тестирования игры.

```python
def generate_treasure_location(self):
    x = random.randint(0, self.size - 1)
    y = random.randint(0, self.size - 1)
    #logging.info(f'Координаты {x}, {y}')
    return (x, y)
```
