# HASH is function takes input and return a fixed-size string of bytes (accurate bytes for string)
tt = (1,2,(30,40))
print(hash(tt))

tt = (1, 2, frozenset([30, 40]))
print(hash(tt))

c = list(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)

class person:
 def __init__(self,name,age):
     self.name = name
     self.age = age
 def __hash__(self):
     return hash((self.name,self.age))

 def __eq__(self, other):
     return (self.name,self.age) == (other.name,other.age)

Person =person("abi",20)
print(hash(Person))


DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]

country = {country: code for code,country in DIAL_CODES}
diccountry = {code: country.upper() for country,code in country.items() }
print(f'{diccountry}')

# import re
# WORD_RE = re.compile('\w+')
# print( WORD_RE)