from random import choice
from random import randint

number = randint(1, 200)

class RandomWalk():
    """Класс для генерации случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блеждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Вычисление следующего шага"""
        """Определение направления и длины перемещения."""
        x_direction = choice([1, -1])
        x_distance = choice([number])
        x_step = x_direction * x_distance
        y_direction = choice([1, -1])
        y_distance = choice([number])
        y_step = y_distance * y_direction

        return x_step, y_step


    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        while len(self.x_values) < self.num_points:
            # Получаеам шаги
            steps = self.get_step()

            # Вычисление следующих значений x и y.
            next_x = self.x_values[-1] + steps[0]
            next_y = self.y_values[-1] + steps[-1]

            # Сохраняем значения
            self.x_values.append(next_x)
            self.y_values.append(next_y)


