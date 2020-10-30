class Employee:
    def __init__(self, first, last, age, sal):
        self.first = first
        self.last = last
        self.age = age
        self.sal = sal
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        # return '{} {}'.format(self.first, self.last)                # stmt 1
        print('{} {}'.format(self.first, self.last))                # stmt 2

    def emp_age(self):
        print('age is {}'.format(str(self.age)))                        # stmt 3
        # return self.age                                             # stmt 4


emp1 = Employee('san', 'kumar', 13, 50000)
emp2 = Employee('sanjay', 'kr', 26, 50000)

# stmt 1
# print(emp1.fullname())
# print(Employee.fullname(emp1))

# stmt 2
emp1.fullname()
Employee.fullname(emp1)

# stmt 3
emp1.emp_age()
Employee.emp_age(emp1)

# stmt 4
# emp1.emp_age()
# print(emp1.emp_age())
