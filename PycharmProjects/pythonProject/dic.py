import random

# d = {1:'one',2:'two',3:'three'}
# v = {4:"four",5:'five',6:'six'}
#
# print({**d,**v})
#
#
# numbers = [2,5,2,1,7,5,9]
#
# un = list(set(numbers))
# print(un)
#
# print(3+random.randrange(11))
#
# # [ ) which means [a,b) range of a include but does not range of include b if ( ] opposite it
# print(R"\nhello")
#
# print("*\t*\t*".expandtabs(100))
# print('{:,}'.format(1112223334))

#  prime


def prime_num(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if i%n == 0:
            return False
    return True

n = 11
if prime_num(n):
        print(n,"is prime number")
else:
    print(n)



def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in numbers:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i!= largest:
            second_largest = i
    return second_largest

# Test the function
nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")


height = [1,8,6,2,5,4,8,3,7]
n = len(height)
r = n-1
l = 0
max_area = 0

while l < r:
    w = r-l
    h = min(height[l],height[r])
    a = w * h
    max_area = max(a,max_area)

    if height[l] < height[r]:
        l +=1
    else:
        r-=1
print(max_area)



