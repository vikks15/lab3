import random

# Генератор вычленения полей из массива словарей
def field(items, *args):
    assert len(args) > 0
    for obj in items:
        if len(args) == 1:
            for el in args:
                if el in obj:
                    yield obj[el]
        else:
            d = {}
            for el in args:
                if el in obj:
                    d[el] = obj[el]
            if len(d) != 0:
                yield d


# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)
