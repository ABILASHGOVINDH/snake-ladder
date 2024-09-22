import bisect
l = [100,4,5,75,9,65,3,5,2,12,46,11,77,85]
lisit = sorted(l)
print(bisect.bisect_right(lisit,12))
print(lisit)
#
def find_prevoius(a,x):
    i = bisect.bisect_left(a,x)
    if len(a) < i:
        return a[i]
    return a[i-1]

nit = find_prevoius([2,3,14,24,32,45,67,88,],33)
print(nit)

# def get_grade(score,cuttoffs=[60,70,80,90], grqades = 'FDCBA'):
#     for i in range(len(cuttoffs)):
#         if score < cuttoffs[i]:
#             return grqades[i]
#     return grqades[-1]
#
#
# grades = [get_grade(score) for score in [52,99,77,100,78,55,66,77]]
# print(grades)
#
# # or bisect method
#
# def get_grade(score,cuttoffs=[60,70,80,90], grqades = 'FDCBA'):
#     i = bisect.bisect_right(cuttoffs,score)
#     return grqades[i]
#
# grades = [get_grade(score) for score in [52,99,77,100,78,55,66,77]]
# print(grades)
#
# import bisect
# import random
# SIZE = 7
# random.seed(1729)
# my_list = []
# for i in range(SIZE):
#  new_item = random.randrange(SIZE*2)
#  bisect.insort(my_list, new_item)
#  print('%2d ->' % new_item, my_list)
# print( )
# print( )
# print( )
# print( )
#
# import random
# size = 7
# my_list = []
# random.seed(1020)
# for i in range(size):
#     new_item = random.randrange(SIZE * 2)
#     my_list.append(new_item)
#     print('%2d ->' % new_item, my_list)
#
#
# m = [1,33,44,56,7,8,55]
# print(bisect.bisect(m,55))
