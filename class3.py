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

    def raise_sal1(self):
        #self.sal = int(self.sal * Employee.raise_per)
        # self.a = 10 * 20
        # self.a = 10 * self.raise_per
        self.a = 10 * Employee.raise_per

        print(self.a)

    def raise_sal(self, data):
        self.sal = int(data * self.raise_per)


emp1 = Employee('san', 'kumar', 13, 50000)

# stmt 1
print(emp1.fullname())
print('***********************')

emp1.raise_sal1()


