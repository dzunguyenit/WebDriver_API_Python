class BasicFunction:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        BasicFunction.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % BasicFunction.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


emp1 = BasicFunction("Zara", 2000)
emp1.displayCount()
emp1.displayEmployee()
