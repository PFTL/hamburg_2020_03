from person import Person


class Student(Person):
    def __init__(self, name, last_name, course):
        super().__init__(name, last_name)
        self.course = course

    def print_enrollment(self):
        print('Is enrolled to', self.course)

    def print_full_name(self):
        print(self.last_name, self.name)

    def old_print_full_name(self):
        super().print_full_name()




if __name__ == '__main__':
    me = Student('Aquiles', 'Carattino', 'Physics')
    me.print_full_name()
    me.old_print_full_name()
    me.print_enrollment()
    print(me.__dict__)


