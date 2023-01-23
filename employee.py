class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return '%s has a salary of %.2f' % (self.name, self.salary)
