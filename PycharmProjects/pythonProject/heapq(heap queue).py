lists = [[1,4,5],[1,3,4],[2,6]]
lists.sort(key =lambda x:x[0])
merge = []

for i in lists:
   merge.extend(i)
print(sorted(merge))

import heapq

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged = list(heapq.merge(*lists))
print(merged)

import heapq

data = [1, 2, 3, 4, 5, 6, 78, 9]
heapq.heappush(data, 0)  # Adds 0 to the heap
print(data)  # Output: [0, 2, 1, 4, 5, 6, 78, 9, 3]

data = [1, 2, 3, 4, 5, 6, 78, 9]
smallest = heapq.heappop(data)
print(data)  # Output: [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]



largest = heapq.nlargest(1, data)
print(largest)

import string
print( string.ascii_letters)
