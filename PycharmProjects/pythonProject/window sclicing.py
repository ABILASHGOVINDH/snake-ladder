# k = [9,1,4,6,8,3,5,7]
# grater = 0
# second_grater = 0
# for i in k:
#     if i > grater:
#         second_grater = grater
#         grater = i
#     if i > second_grater and i != grater:
#         second_grater = i
# print(second_grater)

s = "PAYPALISHIRING"
numRows = 3
n =len(s)
rows = ['']*n
index = 0
direction = 1

for i in s:
    rows[index] += i
    if index == 0:
        direction =1
    elif index == numRows-1:
        direction = -1
    index += direction
print(''.join(rows))