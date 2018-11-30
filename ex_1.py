#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Стул', 'color': 'white'},
    {'color': 'red'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1

# ex1 = field(goods, 'title')
# for item in ex1:
#     print(item, end=', ')

print(', '.join(field(goods, 'title')), '\n')

for item in field(goods, 'title', 'price'): print(item, end=' ')
print()

for item in gen_random(1, 3, 5): print(item, end=' ')
print()
