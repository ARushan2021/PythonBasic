class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def Last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: ' + self.name + ', ' + str(self.pay) + ']'

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self,name, 'mgr', pay)

    def give_raise(self, percent, bonus=100):
        Person.give_raise(self, percent + bonus)

ivan = Person('Иван Petrov', pay=50)
john = Person('John Sidorov', job='dev', pay=100000)


john.give_raise(.10)
ivan.give_raise(0.05)

print(ivan)
print(john)

tom = Manager('Tom Jones', 50000)
tom.give_raise(0.10)
print(tom)