#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']

# Реализация задания 2
unique1 = Unique(data1)
for el in unique1:
    print(el, end=' ')

print()

unique2 = Unique([item for item in data2])
for el in unique2:
    print(el, end=' ')

print()

unique3 = Unique(data3, ignore_case=True)
for el in unique3:
    print(el, end=' ')

print()

unique3 = Unique(data3)
for el in unique3:
    print(el, end=' ')
