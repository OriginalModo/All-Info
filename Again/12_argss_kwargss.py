# позиционные аргументы всегда идут вначале
# / - всё что слева - только позиционные аргументы
# *, - всё что справа - только keyward аргументы
# *args собирает все позиционные аргументы в кортеж
# *kwargs собирает все keyward аргументы в словарь

#1) args и kwargs в параметрах функции - общепринятые имена, но можно использовать и другие
# 2) позволяет распаковать iterable/sequence, а ** распакуют словарь
# 2) Итерируемый объект (iterable) - это объект, который способен возвращать элементы по одному
# 2) Последовательность (sequence) - это итерируемый объект, к элементам которого можно обратиться по целочисленному
# индексу, а также можно узнать общее количество элементов (длину последовательности)
# 3) если нет никаких спецсимволов, то аргументы функции можно передавать как позиционно, так и keyword (то есть ключ=значение).
# Важно помнить, что позиционные всегда идут раньше keyword,
# при этом keyword аргументы между собой не обязаны хранить порядок.
# 4) спецсимвол / в параметрах функции говорит, что все, что ДО него должно передаваться как позиционные аргументы
# 5) спецсимвол * (без указания переменной), говорит о том что все, что ПОСЛЕ него должно передаваться как keyword аргумент
# 6) *args в параметрах функции соберет все позиционные аргументы в кортеж (tuple)
# 7) **kwargs в параметрах функции соберет все keyword аргументы в словарь (dict)


a, *b, c = 'abcd'


def example(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


def my_print(*args, **kwargs):
    print(f'Got keywords: {kwargs}')
    for arg in args:
        print(str(arg), **kwargs)




if __name__ == '__main__':
    # my_print(1, 2, 3, 4, 5, sep=':', end='-')
    print(1,2, **{'sep':':', 'end': '-'})

    # print(*[1, 2, 3])
    # example(1, 2, d=True, c=False)
