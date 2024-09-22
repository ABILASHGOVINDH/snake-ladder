lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

for passport in traveler_ids:
    print( '%s:%s' % passport)


print()

metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]

fmt = '{:16}|{:^10}|{:^10}'
for name,kk,ll,(latitude, longitude) in metro_areas:
    if longitude <=0:
      print( fmt.format (name,latitude,longitude))


print()

name = "abi"
age =30

print('%s:%s' % (name,age))
print()
print()

student = [('ABILASH','UG','CES','VELS')]

fmt = '{:7} | {:^3} | {:^3} | {:4}'
for name,degree,department,clgname in student:
    print(fmt.format(name,degree,department,clgname))

t = (20, 8)
print(divmod(*t))

print(pow(4,2))

print()

from collections import namedtuple

topics = namedtuple('topics','name degree department clgname')
std = topics('ABILASH','UG','CES','VELS')
print(std)



from collections import namedtuple

# Define a namedtuple type
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Create an instance of the namedtuple
person_instance = Person('Alice', 30,'Female')

# Accessing the fields
print(person_instance.name)  # Output:

e= ('1')
s= ('1','ouwebfuobewd''1','1','1','1',',2,3,4,5,6')
s_list = list(s)
s_list.sort(key=None, reverse=False)
print(s_list)
print(e in (s,),)
p = ['1','2','3','4']
print(p.pop(1))
print(e.count('1'))
