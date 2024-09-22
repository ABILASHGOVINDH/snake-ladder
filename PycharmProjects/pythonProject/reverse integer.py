x = 1534236469
reverse = 0
sign = -1 if x<0 else 1
x = abs(x)
while x != 0:
    res = x%10
    reverse = reverse*10+res
    x //= 10
reverse *= sign
if reverse > 2**31 -1 or reverse < 2**31:
    print(0)

print(reverse)