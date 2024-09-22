class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        for i in range(len(s)):
            if i < len(s)-1 and s[i] < s[i+1]:
                value -= d[s[i]]
            else:
                value +=d[s[i]]

        return value

sol = Solution()
s = 'IX'
print(sol.romanToInt(s))