import time

# Контекстный менеджер timer
# после выполнения блока он должен вывести время выполнения в секундах


class timer:
    def __enter__(self):
        self.then = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.then)

