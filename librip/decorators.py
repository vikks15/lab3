# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно

def print_result(func_to_decorate):
    def decorated_func(*args):
        print(func_to_decorate.__name__)
        func = func_to_decorate(*args)
        if type(func) is list:
            for el in func:
                print(el)
        elif type(func) is dict:
            for key, value in func.items():
                print('{} = {}'.format(key, value))
        else:
            print(func)
        return func
    return decorated_func
