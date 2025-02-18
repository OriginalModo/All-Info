# Из важного:
# 1) исключения это нормальный и важный механизм в питоне, не нужно стесняться его использовать, бросать и
# перехватывать исключения, писать свои типы исключений. К сожалению, по ряду причин не редко вижу,
# что программисты не кидают исключений в своих функциях
# 2) когда пишем функции, то стараемся думать не в позитивном ключе, а в плане того, что может пойти не так.
# В таких случаях бросаем исключения, делаем это как можно раньше (в начале функции)
# 3) Механизм по-умолчанию в питоне просто выведет текст исключения и завершит работу программы,
# если нам нужно другое поведение то используем try/except/finally
# 4) блоков except может быть несколько, каждый со своим типом исключения и логикой,
# но важно чтобы исключение было конкретным, и в блоке всегда делаем хоть что-то. НЕ проглатываем исключения!
# 5) finally выполняется в любом случае, даже если исключения не упало, НО важно понимать,
# что файналли это не какой то волшебный блок, исключение может упасть и там,
# нужно обдумывать логику этого блока (например не использовать переменные, которые могли не быть созданы)
# 6) raise используем чтобы бросить исключение самостоятельно,
# при этом можно указать какое конкретно исключение бросить.
# Если не указать то будет брошено последнее упавшее исключение (важно чтобы оно было!)
# 7) не стесняемся писать свои классы исключений,
# главное давать им понятные имена и прописываем в доке случаи, когда они могут быть выброшены

class ArgumentEqualZeroError(Exception):
    """When argument == zero"""
    pass


class ArgumentIsNotIntegerError(Exception):
    """When argument no Int"""
    pass


def divide(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentIsNotIntegerError('Must be ints')
    if b == 0:
        raise ArgumentEqualZeroError("No ZERO")
    return a // b


if __name__ == '__main__':
    try:
        print(divide(4, 0))
    except (ArgumentIsNotIntegerError, ArgumentEqualZeroError) as exc:
        print(exc)
    finally:
        print('Finish')
