i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
print()
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


print('')
def counters(s):
    feq = {}
    for char in s:
        feq[char] = feq.get(char,0)+1
        print(feq[char])
    for index, char in enumerate(s):
        if feq[char] == 1: # 1 would give you k single string or # 2 would give you double string e,t,n
            print('index:',index,'char:',char)
        feq[char] += 1
    return -1

s= 'eettknn'
counters(s)