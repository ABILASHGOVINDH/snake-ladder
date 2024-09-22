a = [1,4,5,6]
x = 10
def has_pair(a  ,x):
    seen = {}
    for i,num in enumerate(a):
        complement = x - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return False

print(has_pair(a,x))