# Инкапсуляция заключается в сборе в одно место (класс) данных и методов для работы с ними и
# предоставлении пользователю публичного интерфейса(API(Публичный интерфейс))
# public(публичный) = без _ , __
# _ - protected(защищенный) знак того, что этот атрибут не предназначен для прямого использования.
# Работа обьекта не гарантируется, при использовании таких атрибутов
# __ - private(приватный) под капотом преобразуется в object._Class__attribute (только для случаев когда начинается с __)
# Name MangLing (Преобразование в не явное)
# Явное лучше неявного!!!
# Публичный АПИ(интерфейс) - это контракт, все методы будут работать, внутренняя же реализация не гарантируется.
# Совет - делать одно _ для врутренних атрибутов и реализаций, не перебарщивать с __ и сеттерами/геттерами


# В питоне применяется нижнее подчеркивание _ для пометки внутренней реализации,
# то есть атрибутов не относящихся к публичному интерфейсу.
#
# Одно подчеркивание (protected) - это всего лишь сигнал, интерпретатор относится к таким атрибутам как к обычным.
# Два подчеркивания (private) - включает механизм подмены имени Name Mangling,
# который предназначен не для сокрытия данных.
#
# Инкапсуляция в питоне не подразумевает сокрытия данных (в некоторых языках это одно и то же)
# - все данные доступны для просмотра и изменения. В Python мы не пробуем отобрать у юзера инструменты, мы предупреждаем.


class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.__age = age

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError('Age must be in range 1-120')
        self.__age = age

    def describe(self):
        print(f'I am {self._first_name} {self._last_name}, Im {self.__age} years old')


if __name__ == '__main__':
    ivan = Person('Ivan', 'Ivanov', 30)
    ivan._Person__age = 100
    # ivan.set_age(120)
    ivan.describe()
    print(ivan._first_name)
    print(dir(ivan))
    print(ivan._Person__age)


