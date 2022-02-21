class InconsistentError(Exception):
    pass
def dot_product(a, b):
    if len(a) != len(b):
        raise InconsistentError(f'Length of args are different ({len(a)}!={len(b)}')
    return sum (i1*i2 for i1, i2 in zip(a, b))