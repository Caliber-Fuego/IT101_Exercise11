from employee import Employee
from manager import Manager
from executive import  Executive


def main():
    employee  = Employee("John Smith", 45000)
    manager   = Manager("Jane Doe", 60000, "Widgets")
    executive = Executive("Weird Guy", 90000, "Thingies")

    print(employee.__repr__())
    print(manager.__repr__())
    print(executive.__repr__())


main()