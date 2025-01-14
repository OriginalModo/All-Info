"""
Многопоточность (Multithreading) Одиночка (Singleton) :

Если из разных потоков обратимся к нашему Singleton то у нас выйдет 2 ЭКЗЕМПЛЯРА класса в системе
"""
from threading import Lock


class SingletonBaseClass(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
