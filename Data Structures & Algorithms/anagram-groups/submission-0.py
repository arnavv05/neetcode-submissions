from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-ord("a")]+=1
            
            key = tuple(count)
            anagram_dict[key].append(str)

        return list(anagram_dict.values())
