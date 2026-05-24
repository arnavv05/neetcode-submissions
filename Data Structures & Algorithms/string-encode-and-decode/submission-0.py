class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+"#"+s 
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            hash_ind = s.find("#", i)
            len_word = int(s[i:hash_ind])
            start_word = hash_ind+1
            end_word = start_word+len_word
            result.append(s[start_word:end_word])
            i = end_word
        return result

        

