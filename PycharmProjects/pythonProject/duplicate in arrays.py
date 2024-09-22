nums = [1,1,2]

# k = 1
# for i in range(1,len(nums)):
#     if nums[i] != nums[i-1]:
#        nums[k] =nums[i]
#        k += 1
# print(k)

k = 0
seen = []
for num in nums:
    if num not in seen:
        seen.append(num)
        k += 1
print(k)