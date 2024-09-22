# a = [2, 1, 2, 4, 3]
# n = len(a)
# stack = []
# res = [-1]*n
#
# for i in range(n-1,-1,-1):
#     while stack and stack[-1] <= a[i]:
#         print(stack.pop())
#     if stack:
#         res[i] = stack[-1]
#     stack.append(a[i])
# print(res)

s = [3,4,-1,2,-3,0]
s = sorted(s,reverse=True)
n = 4
missing = 1
s_set = set(s)
while missing in s:
    missing += 1
largest = s[:n-1]
max_sum = sum(largest) + missing
print(max_sum)












# result = []
# s = sorted(s)
# final = 0
# for i in s:
#     if i > 0:
#         result.append(i)
# for i in range(len(result)):
#     final += result[i]
#
# print(final)