x = 121
revers = 0
while x != 0:
  digit = x % 10
  revers = revers * 10 + digit
  x //= 10
print(revers)


class Solution:
  def isPalindrome(self, x: int) -> bool:
    y = x
    reverse_num = 0
    while y != 0:
      digit = y % 10
      reverse_num = reverse_num * 10 + digit
      y //= 10

    if reverse_num == x:
      return True
    else:
      return False


x = 111
sol = Solution()
print(sol.isPalindrome(x))
class Solution:
    def romanToInt(self, s: str):
        value = 0
        d = {'I': 1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000,}
        for i in range(len(s)):
            if i<len(s)-1 and d[s[i]] < d[s[i+1]]:
                value -= d[s[i]]
            else:
                value += d[s[i]]

# or
        ans = d[s[-1]]
        for i in range(len(s)-2,-1,-1):
           if d[s[i]] < d[s[i+1]]:
               ans -= d[s[i]]
           else:
               ans += d[s[i]]
        return ans
sol = Solution()
s = 'MCMXCIV'
print(sol.romanToInt(s))