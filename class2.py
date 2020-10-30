class Employee:
    raise_per = 1.04

    def __init__(self, first, last, age, sal):
        self.first = first
        self.last = last
        self.age = age
        self.sal = sal
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)                # stmt 1

    # Employee.raise_per in below both method has different concept: self.
    # riase_per can be changed by other method or inherited class but not Employee.raise_per.

    def raise_sal1(self):
        self.sal = int(self.sal * Employee.raise_per)

    def raise_sal(self, data):
        self.sal = int(data * self.raise_per)


emp1 = Employee('san', 'kumar', 13, 50000)

# stmt 1
print(emp1.fullname())
print(Employee.fullname(emp1))

print('-----------------------')
print(emp1.sal)
emp1.raise_sal1()
print(emp1.sal)

print('-----------------------***')
print(emp1.sal)
emp1.raise_sal(100)
print(emp1.sal)


print('-----------------------*** Verify what class contain ***------------')
print(emp1.__dict__)

print('-----------------------*** Verify what class contain ***------------')

print(Employee.__dict__)