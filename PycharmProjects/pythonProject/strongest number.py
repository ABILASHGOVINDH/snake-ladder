# import math
#
# def is_strogest(num):
#     print(type(num))
#     str_num = str(num)
#     sum_of_factorial =0
#     for digits in str_num:
#         sum_of_factorial+=math.factorial(int(digits))
#
#     return sum_of_factorial == num
#
#
# numbers = [1,2,145,40585,3]
# strog = [num for num in numbers if is_strogest(num)]
# print(strog)

# or
import math
def strongest(num):
    digits = list(map(int,str(num)))
    sum_of_strongestnum = sum(math.factorial(digit) for digit in digits)
    return sum_of_strongestnum == num

numbers = range(1,100000000)
strong = [num for num in numbers if strongest(num)]
print(strong)



# print( )
# # list comprehension
# squares = [x**2 for x in range(10)]
# print(squares)
#
# print()
# #simple way
#
# import math
#
# def strongest_num(num):
#     return sum(math.factorial(int(digit)) for digit in str(num)) == num
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if strongest_num(num):
#        print(num)
# print()
#
# # without using math and using logic
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)
#
# def sum_factorials(num):
#     if num == 0:
#         return 0
#     else:
#         return factorial(num % 10) + sum_factorials(num // 10)
#
# def strongest_num(num):
#     return sum_factorials(num) == num
#
#
# numbers = [0,1,2]
# for num in numbers:
#     if strongest_num(num):
#         print(num)
#
#
# factori = lambda n:1 if n == 0  else n * factori(n-1)
# sum_of_factori = lambda num :0 if num == 0 else factori(num % 10) + sum_of_factori(num //10 )
#
# def refact(limit):
#     strongest_num = []
#     for num in range(0,limit):
#         if num == sum_of_factori(num):
#           strongest_num.append(num)
#     return strongest_num
#
# limit = 146
# strongest_num = refact(limit)
# print(strongest_num)