class Employee:
    def __init__(self, first, last, age, sal):
        self.first = first
        self.last = last
        self.age = age
        self.sal = sal
        self.email = first + '.' + last + '@gmail.com'

    def marks(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.total = sub1 + sub2 + sub3
        return self.total


emp1 = Employee('san', 'kumar', 13, 50000)
emp2 = Employee('sanjay', 'kr', 26, 50000)

print(emp1.email)
print('Firstname:  {} Lastname: {} Age: {} Email: {}'.format(emp1.first, emp1.last, emp1.age, emp1.email))
print('Firstname:  {} Lastname: {} Age: {} Email: {}'.format(emp2.first, emp2.last, emp2.age, emp2.email))


test = Employee.marks()
print(Employee.marks(test,12, 12, 12))


# print(marks1.total)


# emp1.name = 'san'
# emp1.age = 23
# emp1.phone = 23423423423
# emp1.sal = 232323
#
#
# emp2.name = 'sanjay'
# emp2.age = 25
# emp2.phone = 222222
# emp2.sal = 50000
#
# print(emp1.name)
# print(emp2.name)
