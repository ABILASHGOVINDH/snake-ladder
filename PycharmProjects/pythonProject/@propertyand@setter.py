# property is converts or change function into attribute and setter set value for it
class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.__email = first+'.'+last+'@email.com'


    @property
    def fullname(self):
        return '{}.{}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
       first,last = name.split(' ')
       self.first = first
       self.last = last



emp1 = Employee('Abi','Govindh')
emp1.fullname = 'jim simth'
print(emp1.fullname)
emp1._Employee__email = 'abiGovindharaju@email.com'
print(emp1._Employee__email)#naming fuction use __ underscore
