from manager import Manager

class Executive(Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self):
        return '%s has a salary of %.2f and is the executive for the %s department' %(self.name, self.salary, self._department)