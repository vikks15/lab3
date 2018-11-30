# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items

        if type(items) is list:
            self.len = len(items)
            self.index = 0
        else:
            self.len = 1
            self.index = 0

        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        if self.index == self.len:
            raise StopIteration

        if self.index != 0:
            count = 0
            while count < self.index:
                if self.ignore_case:
                    if self.items[self.index].lower() == self.items[count].lower():
                        self.index += 1
                        return
                else:
                    if self.items[self.index] == self.items[count]:
                        self.index += 1
                        return
                count += 1

        currentIndex = self.index
        self.index += 1
        return self.items[currentIndex]

    def __iter__(self):
        return self
