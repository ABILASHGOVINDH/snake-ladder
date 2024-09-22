# import textwrap
from collections import Counter
# a = [1,3,4,4,8,6,8]
# coun = Counter(a)
#
# for n,i in coun.items():
#     if i == 1:
#         print(n,end=' ')
#
# print()
# print()
#
# r =0
# for i in a:
#    r = r ^ i
# print(r)
# print()
# print()
# print()
# print()
# class Solution:
#     def singleNumber(self, nums):
#         res = 0
#         for n in nums:
#             res = n ^ res
#         return res
# sol = Solution()
#
# print(sol.singleNumber([1,3,4,4,8,6]))
#
# s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# width = 4
#
# c = textwrap.wrap(s,width)
# print('\n'.join(c))
#
#
# v = 'HackerRank.com presents "Pythonist 2".'
# print(v.swapcase())
#
# s = [2, 3, 6, 5]
# result = 0
#
# # XOR all numbers to find the unique one
# for number in s:
#     result ^= number
#
# print( result)

# prefix _sum
#
# def prefix_sum(n):
#       prefix =[0]*(len(n)+1)
#       for i in range(len(n)):
#             prefix[i+1] += prefix[i] + n[i]
#       prefix_s = prefix[29] - prefix[14]
#       return prefix_s
#
# numbers = [2, 8, 9, 11, 12, 26, 27, 29, 33, 36, 37, 42, 44, 46, 47, 52, 56, 57, 58, 60, 61, 64, 68, 70, 72, 73, 76, 77, 78, 80, 82, 83, 95, 96, 98, 99]
#
# print(prefix_sum(numbers))
#
#
# class NumArray:
#
#     def __init__(self, nums):
#         self.prefix = [0] * (len(nums) + 1)
#         for i in range(len(nums)):
#             self.prefix[i + 1] += self.prefix[i] + nums[i]
#     def sumRange(self, left: int, right: int):
#         return self.prefix[right+1] - self.prefix[left]
#
#
# nums =[-2,0,3,-5,2,-1]
# n = NumArray(nums)
# print(n.sumRange(0,2),end='')
# print(n.sumRange(2,5),end='')
# print(n.sumRange(0,5),end='')
l = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(l)
max_con = float('-inf')  # Initialize to negative infinity to handle all negative cases

for i in range(n):
    cum = 0  # Start cum at 0 for each new starting point i
    for j in range(i, n):
        cum += l[j]  # Add l[j] to cum to extend the subarray from i to j
        max_con = max(max_con, cum)  # Update max_con if cum is greater

print(max_con)
