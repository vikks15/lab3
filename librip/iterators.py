# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.len = len(items)
        self.index = 0

        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index == self.len:
                raise StopIteration

            before_ind = self.index

            if self.index != 0:
                count = 0
                while count < self.index:
                    if self.ignore_case:
                        if self.items[self.index].lower() == self.items[count].lower():
                            self.index += 1
                            break
                    else:
                        if self.items[self.index] == self.items[count]:
                            self.index += 1
                            break
                    count += 1

            if before_ind == self.index:
                self.index += 1
                return self.items[before_ind]

    def __iter__(self):
        return self
