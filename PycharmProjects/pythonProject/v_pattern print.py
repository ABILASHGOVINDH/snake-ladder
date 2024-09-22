n=12

for k in range(n):
   print(" "*k+"1"+" "*(2*(n-k-1)-1)+("13" if k< n-1 else "13"))