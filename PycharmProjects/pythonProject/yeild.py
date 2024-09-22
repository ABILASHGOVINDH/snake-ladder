def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
for value in gen:
    print(value)

def fibinocci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b = b,a+b


fic = fibinocci(22)
for num in fic:
    print(num)