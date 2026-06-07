class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        l = 0
        sett = set()
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            w = r-l+1
            longest = max(longest, w)
        return longest