import re


PREFIXES = {
    'decimal': [
        ('k', 1000 ** 1),
        ('M', 1000 ** 2),
        ('G', 1000 ** 3),
        ('T', 1000 ** 4),
        ('P', 1000 ** 5),
        ('E', 1000 ** 6),
        ('Z', 1000 ** 7),
        ('Y', 1000 ** 8),
    ],
    'binary': [
        ('Ki', 1024 ** 1),
        ('Mi', 1024 ** 2),
        ('Gi', 1024 ** 3),
        ('Ti', 1024 ** 4),
        ('Pi', 1024 ** 5),
        ('Ei', 1024 ** 6),
        ('Zi', 1024 ** 7),
        ('Yi', 1024 ** 8),
    ]
}

PREFIXES = {
    system: [
        (
            prefix[0],
            prefix[1],
            re.compile('(\d+){}'.format(prefix[0])),
        )
        for prefix in prefixes
    ]
    for system, prefixes in PREFIXES.items()
}


def to_number(string):
    for system, prefixes in PREFIXES.items():
        for prefix in prefixes:
            match = re.match(prefix[2], string)
            if match:
                return float(match.group(1)) * prefix[1]
    return float(string)

def to_string(number, system='decimal'):
    for sys, prefixes in PREFIXES.items():
        if sys != system:
            continue
        for prefix in prefixes[::-1]:
            if number >= prefix[1]:
                digit = number // prefix[1]
                number -= prefix[1] * digit
                return '{}{}{}'.format(digit, prefix[0], number if number else '')
    return str(number)
