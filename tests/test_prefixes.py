import pytest

from prefixes import to_number, to_string


@pytest.fixture(params=[10 ** power for power in range(3)])
def number(request):
    return request.param

@pytest.fixture(
params=[
    ('',  1000 ** 0, 'decimal'),
    ('k', 1000 ** 1, 'decimal'),
    ('M', 1000 ** 2, 'decimal'),
    ('G', 1000 ** 3, 'decimal'),
    ('T', 1000 ** 4, 'decimal'),
    ('P', 1000 ** 5, 'decimal'),
    ('E', 1000 ** 6, 'decimal'),
    ('Z', 1000 ** 7, 'decimal'),
    ('Y', 1000 ** 8, 'decimal'),
    ('Ki', 1024 ** 1, 'binary'),
    ('Mi', 1024 ** 2, 'binary'),
    ('Gi', 1024 ** 3, 'binary'),
    ('Ti', 1024 ** 4, 'binary'),
    ('Pi', 1024 ** 5, 'binary'),
    ('Ei', 1024 ** 6, 'binary'),
    ('Zi', 1024 ** 7, 'binary'),
    ('Yi', 1024 ** 8, 'binary'),
],
ids=[
    '',
    'kilo',
    'mega',
    'giga',
    'tera',
    'peta',
    'exa',
    'zetta',
    'yotta',
    'kibi',
    'mebi',
    'gibi',
    'tebi',
    'pebi',
    'exbi',
    'zebi',
    'yobi',
])
def prefix(request):
    return request.param

class TestPrefixes(object):
    def test_to_number(self, number, prefix):
        if(
            prefix[0] == 'Y' and
            number == 10
        ):
            pytest.xfail('Interpreter precision?')
        assert to_number(str(number) + prefix[0]) == float(number * prefix[1])

    def test_to_string(self, number, prefix):
        assert to_string(number * prefix[1], system=prefix[2]) == str(number) + prefix[0]

    def test_extra_digits_after_prefix(self):
        assert to_number('1k5') == 1005
        assert to_string(1005) == '1k5'
