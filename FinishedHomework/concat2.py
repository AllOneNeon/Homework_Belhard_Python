
def concat (*args:str, **kwargs) -> str:
    if True in kwargs.values():
        result = ("".join([i for i in args[::-1]]))
    else:
        result = ("".join([i for i in args]))
    return (result)
x = list(map(str,input(
    'Введите любые слова через запятую: ').split(',')))
y = bool(input(
    '''Введите значение параметра reversed: Нажмите на любую клавишу и затем "Enter", если "True".
       Нажмите только "Enter", усли "False" ''' ,))

def inspect(f):
    def inside (*args, **kwargs):
        reprval = f(*args, **kwargs)
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        print(f'reprinting_values {reprval}')
        return reprval
    return inside

concat = inspect(concat)
concat (*x, reversed=y)
