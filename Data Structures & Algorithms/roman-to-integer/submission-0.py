class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I":1,
                     "V":5,
                     "X":10,
                     "L":50,
                     "C":100,
                     "D":500,
                     "M":1000}
        result = 0
        n = len(s)
        for i in range(n):
            if i<len(s)-1 and roman_num[s[i]]<roman_num[s[i+1]]:
                result -= roman_num[s[i]]
            else:
                result += roman_num[s[i]]
        return result