arr1 = [1, 5, 9, 10, 15]
arr2 = [2, 3, 8, 13]
n = len(arr1)
m = len(arr2)

def merge(arr1,arr2,n,m):
    i =n-1
    j = 0
    while i>=0 and j<m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        else:
            break

    arr2.sort()
    arr1.sort()

merge(arr1,arr2,n,m)


print("Merged arr1:", arr1)
print("Merged arr2:", arr2)


arr1 = [1, 5, 9, 10, 15]
arr2 = [2, 3, 8, 13]

combine = arr1+arr2
combine.sort()
n = len(arr1)
arr1[:] = combine[:n]
arr2[:] = combine[n:]

print(arr1)
print(arr2)

