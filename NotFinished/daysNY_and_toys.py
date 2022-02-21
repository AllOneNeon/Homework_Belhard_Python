import click
from datetime import datetime
import random

NY_date = datetime(2023, 1, 1)

toys = ['bear', 'santa', 'ball', 'angel', 'tree', 'star', 'candy', 'snowlake']
colors = ['green', 'red', 'yellow', 'white', 'blue', 'purple', 'orange', 'black']

@click.group()
def cli():
    pass

@click.command()
@click.option('--hours', is_flag=True, help='Если нужны еще и часы до НГ')
def newyear(hours):
    delta = NY_date - datetime.now()
    if hours:
        return (print(f'До НГ осталось {delta.days} дней и {round(delta.seconds/3600,1)} часов'))
    else:
        return (print(f'До НГ осталось {delta.days} дней'))

@click.command()
def toy():
    t1 = random.choice(toys)
    c1 = random.choice(colors)
    print(f'{c1} {t1}')

cli.add_command(newyear)
cli.add_command(toy)

cli.main()