def buble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0,n-1):
            if num[j]>num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    print(num)


num = [64, 34, 25, 12, 22, 11, 90]
buble_sort(num)
