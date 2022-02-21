from enum import Enum
import random
import click


class Colors (Enum):
    black = 1
    purple = 2
    white = 3
    red = 4
    green = 5
    orange = 6


class Toys (Enum):
    star = 1
    ball = 2
    dedmoroz = 3
    christ = 4
    play = 5
    box = 6

toy = Toys
list(toy)
col = Colors
list(col)


rand_col_id = random.choice(list(col))
rand_t_id = random.choice(list(toy))

print(rand_col_id, rand_t_id)