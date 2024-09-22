arr = [1,2,3,4,-5]
max_current = arr[0]

for i in range(1,len(arr)):
   max_current = max(arr[i],max_current+arr[i])

print(max_current)