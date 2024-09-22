arr = [1, -2, -3, 0, 7, -8, -2]
min_arr = arr[0]
max_arr = arr[0]
result = arr[0]

for i in range(1,len(arr)):
   current = arr[i]
   if current <0:
      max_arr,min_arr = min_arr,max_arr

   max_arr= max(current, max_arr*current)
   min_arr = min(current, min_arr * current)

   result = max(max_arr,result)

print(result)

