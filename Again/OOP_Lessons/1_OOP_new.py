# Обьект - сущность, обьединяющая данные и методы для работы с ними (состояние и поведение)
# Чертеж-класс, обьект это дом
# Класс - это новый тип данных, обьект - его конкретный представитель
# у любого обьекта есть id (адресс в памяти), значение и тип
# первая потребность для классов - когда не хватает встроенных типов, вторая - разное состояние
# метод - это функция которая принадлежит классу
# self - ссылка на экземпляр класса
# dunder(double under) дандер(двойное нижнее подчеркивание), магический метод
# если класс пустой(pass) сравнивает == через is по адресу в памяти (ссылка)


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def meaw(self):
        print(f'{self.name} says: Meow')




if __name__ == '__main__':
    tom = Cat('Tom', 2)
    angela = Cat('Angela', 1)
    print(tom)
    print(angela)
    tom.meaw()
    angela.meaw()
    print(tom.name)
    print(tom.age)
    # Cat.meaw(tom)





