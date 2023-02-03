#Roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and my_dict[s[i]] < my_dict[s[i+1]]:
                ans -= my_dict[s[i]]
            else:
                ans += my_dict[s[i]]

        return ans
            