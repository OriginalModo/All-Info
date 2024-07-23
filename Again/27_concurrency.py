# Конкурентность (concurrency) - запуск на выполнение сразу нескольких задач
# (не обязательно в 1 момент времени выполняется несколько). Зависит от ПО Первые ОС с процессором без ядер -использовали только ее.
# Проще говоря быстрое переключение между задачи

# Параллельность (parallel) - конкурентность, когда 2+ задачи выполняются одновременно. Зависит от железа
#  Вы не можете одновременно (!) выполнять больше задач, чем есть ядер в системе.

# thread-safe - потокобезопасность, означает что при работе с обьектом не возникают известные проблемы
# при работе с конкурентностью

# GIL (Global Interpreter Lock) - глобальная блокировка интерпретатора -
# механизм гарантирующий, что в любой момент времени выполняется только 1 инструкция в питоне.

# GIL - Гарантирует нам что в один момент времени в Python работает РОВНО 1 ПОТОК(инструкция),
# даже если потоков больше

# Подсчет ссылок Этот метод отслеживает количество ссылок, указывающих на каждый объект.
# Когда счетчик ссылок для объекта достигает нуля, что означает их отсутствие,
# объект считается “мусором” (ненужным), он уничтожается сборщиком мусора и память освобождается

# Для всех объектов в программе Python ведется подсчет ссылок. Счетчик ссылок на объект увеличивается всякий раз,
# когда ссылка на объект записывается в новую переменную или когда объект помещается в контейнер, такой как список,
# кортеж или словарь

# Счетчик ссылок (отслеживает создание/удаление обьектов) - ПОТОКОНЕБЕЗОПАСЕН не умеет работать чтобы сразу
# 2 потока сразу создавали или удаляли обьекты

# Задачи могут быть:
# CPU-bound - зависит от мощности процессора # расчеты внутри python власть GIL
# IO-bound - зависит от системы ввода/вывода # обращение к файлу, обращение к сайту # GIL не трогает

# threading - IO-bound задачи # GIL не помешает
# asyncio - IO-bound задачи , 1 поток использует Конкурентность (concurrency) по полной
# multiprocessing - любые задачи

# Книги: Мартин Фаулер

import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def activity():
    # for i in range(100_000):
    #     abs(round(i ** 2 / 122) + i * 3.14)
    requests.get('https://yandex.ru')
    print('OK')


def run(threaded=False):
    start = time.time()
    if not threaded:
        for i in range(10):
            activity()
    else:
        executor = ThreadPoolExecutor()
        for _ in range(10):
            executor.submit(activity)
        # threads = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        # for i in threads:
        #     i.start()
        # for i in threads:
        #     i.join()
        executor.shutdown(wait=True)
    end = time.time()
    print(f'Time: {end - start} seconds')


if __name__ == '__main__':
    run(threaded=True)