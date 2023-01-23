from employee import Employee


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return '%s has a salary of %.2f and manages the %s department' %(self.name, self.salary, self._department)
