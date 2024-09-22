n = 2
for i in range(n):
    for k in range(n,0,-1):
        for j in range(n-i):
            print(k,end=" ")
    print("\n",end="")




k =[{2, 1, 4, 3},
     {1, 2, 3, 2},
     {3, 6, 2, 3},
     {5, 2, 5, 3}]

common = k[0]
for i in k[1:]:
    common &= i
print(common)

n = int(input("enter the number: "))
reverse = 0
while n > 0:
    rem = n%10
    reverse = (reverse*10) + rem
    n = n//10
print("reversed:",reverse)

# fbinocci
s = 100
a,b =1,2
while a < s:
    print(a)
    a,b =b,a+b


# common divisor
a = int(input("enter the number: "))
b = int(input("enter the number: "))

if a > b:
    small = b
else:
    small =a
for i in range(1,small+1):
    if (a%i ==0) and (b%i ==0):
        f = i

print(f)

n = int(input(" enter the number: "))
total = 0
for i in range(1,n+1):
    if n%i==0:
       total += 1
print(total)
