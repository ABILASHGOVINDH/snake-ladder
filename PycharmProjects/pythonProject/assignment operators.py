def assifn(s,n):
   print(s+n)

nike =lambda s,n:s/n
print(nike)


print(nike(3,6))
s=3
n=5
assifn(s,n)


numbers = [1, 2, 3, 4, 5]
a = lambda x: x % 2 == 0
even = []
for num in numbers:
     if a(num):
       even.append(num)


print(even) # Output: [2, 4]


numbers = [1, 2, 3, 4, 5]
n =  lambda x, y: x + y
sum_all = numbers[0]
for num in numbers[1:]:
   sum_all = n(sum_all,num)



print(sum_all)  # Output: 15

def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x < y

print(add(2, 3))         # Output: 5
print(add_lambda(2, 3))







points = [(2, 3), (1, 2), (4, 1), (3, 3)]
points_sorted = sorted(points, key=lambda x: x[0])
print(points_sorted)  # Output: [(4, 1), (1, 2), (2, 3), (3, 3)]
