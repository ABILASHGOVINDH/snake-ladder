s = [1,3,2]
n = len(s)

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if s[i] < s[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

s = [2,2,1]
res =0
for num in s:
    res ^= num
print(res)