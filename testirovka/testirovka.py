from unittest import TestCase
from tests import tests

class DotProfuctTestCase(TestCase):
    def tests_onevalues(a, b):
        return sum (i1*i2 for i1, i2 in zip(a , b))
        assert result == 42, f'result should be 42, not {result}'

    #return a[0] * b[0]
    #return sum (i1 *i2 in i1, i2 in zip(a, b))

    def tests_twovalues():
        result = dot_product([1, 5], [2, 8])
        assert result == 42, f'result should be 42, not {result}'