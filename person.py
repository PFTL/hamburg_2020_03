class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.age = None

    def print_full_name(self):
        print(self.name, self.last_name)

    def calculage_age(self, birth_year):
        age = 2020 - birth_year
        self.age = age

    def print_age(self, birth_year=None):
        if birth_year is not None:
            print('WARNING, birth_year should no longer be used')
        if self.age is None:
            print('You must first run calculate_age')
        else:
            print(self.age)


if __name__ == '__main__':
    me = Person(name='Aquiles', last_name='Carattino')
    me.print_full_name()
    me.calculage_age(1986)
    me.print_age(1986)

    you = Person(name='John', last_name='Doe')
    you.print_full_name()
    you.print_age()
