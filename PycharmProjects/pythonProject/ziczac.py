# def zigzag(n,num):
#     if num == 1:
#         return n
#
#     row = [""]*num
#     index =0
#     direction = 1
#     for i in n :
#         row[index] += i
#
#         if index == 0:
#             direction = 1
#         elif index == num-1:
#             direction = -1
#         index += direction
#     return "".join(row)
#
# print(zigzag("ABCDXYZ",3))
#
# i = 2j +3
# j = 2J +3
# print(type(i))
# print(i+j)


def convert(s, numRows) -> str:
    if numRows == 1:
        return s
    row = [""] * numRows
    index = 0
    direction = 1
    for i in s:
        row[index] += i
        if index == 0:
            direction = 1
        elif index == numRows - 1:
            direction = -1
        index += direction
    return "".join(row)

print(convert(s = "PAYPALISHIRING", numRows = 3))