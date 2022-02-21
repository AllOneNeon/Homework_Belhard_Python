
def inspect(f):
    def inside (*args, **kwargs):
        res = f(*args, **kwargs)
        print(f'''Args: {args}
        kwargs: {kwargs}'
        reprinting_values: {res}''')
        return res
    return inside

@inspect
def concat (*args:str, reversed:bool) -> str:
    result = ''
    if reversed == True:
        for i in args[::-1]:
            result += i
    else:
        for i in (args):
            result += i
    return (result)

concat ('First',' ', 'Second',' ', 'Third', reversed=True)
        