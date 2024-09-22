
print(len('test'))
# or
print('bus'.__len__())
print(int.__rtruediv__(3,27))

class demo:
    def __init__(self,name,book_name,page):
        self.name =name
        self.book_name =book_name
        self.page =page
    def __len__(self):
        return self.page
    def __str__(self):
        return f"bookname: {self.book_name} by name:{self.name}"

d = demo("jenny","python basic to advance",300)
print(len(d))


class author:
    def __init__(self,plus=0):
        self.plus = plus
    def __call__(self,a,b):
        self.plus = a*b
    def __gt__(self,a,b):
        return  a<b

d = author()
d(3,5)
print(d.plus)
print(list.__gt__([5],[6]))
print(d.__gt__(5,6))


class Employee:
    rais_amount = 1.04
    role_num =0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+'@company.com'

        Employee.role_num +=1

emp1 = Employee('Abilash','govindh','35000')
emp2 = Employee('Avinash','govindh','40000')
emp1.rais_amount =1.05
print(emp1.__dict__)
print(Employee.role_num )

# check the data and return it if not exists return the user given missing
class defaultdict(dict):
    def __missing__(self, key):
        return '0 __missing__'
        # or

        # value = []
        # self[key] =value
        # return value


d =defaultdict(a=1,b=2)
print(d['ab'])