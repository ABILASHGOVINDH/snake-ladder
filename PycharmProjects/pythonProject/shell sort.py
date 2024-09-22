s = [23,29,15,19,31,7,9,5,2]
n =len(s)
gap = n//2

while gap > 0:
    for i in range(gap,n):
        tem = s[i]
        j = i
        while j >= gap and s[j-gap] > tem:
          s[j] = s[j-gap]
          j -= gap
        s[j] = tem
    gap //= 2
print(s)

