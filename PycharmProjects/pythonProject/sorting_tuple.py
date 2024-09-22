tup = [(3,5),(1,9),(2,8),(0,5),(9,6)]

for i in range(len(tup)):
    for j in range(len(tup)):
        if tup[i] < tup[j]:
            tup[i],tup[j] = tup[j],tup[i]

print(tup)