a = "sorry mam"
print(list(map(len,a.split(" "))))

list1 = ["1","feint","happy","because","i"]
list2 = [10,20,30,40,50,60]
print((list(map(lambda x,y:str(x)+":"+str(y),list1,list2))))


list1.extend(map(str,list2))
print(list1)

l = [10,8,5,2,3,1]
for i in range(len(l)):
    for j in range(len(l)):
        if l[j] > l[i] :
            l[i],l[j] = l[j],l[i]

print(l)




