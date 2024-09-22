# num = int(input("Enter number:"))
# binary  = num
# decimal = 0
# base = 1
#
# while num >0:
#     rem = num % 10
#     decimal = decimal + rem * base
#     num = num // 10
#     base = base *2
#
# print(f"Binary.no: {binary}\nDecimal.no:{decimal}" )


strs = ["flower", "flow", "flight"]
q =''
for s in zip(*strs):
   print(s)
   if len(set(s)) == 1:
      q+=s[0]
   else:
      print(q)
print(q)

r = strs[-1]
l = strs[0]
prefix = ''
for i in range(min(len(r),len(l))):
   if r[i] == l[i]:
      prefix += r[i]
   else:
      break
print(prefix)