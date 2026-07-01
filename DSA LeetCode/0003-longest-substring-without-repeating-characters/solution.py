class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        max_len = 0
        different_char = set()
        for index in range(len(s)):
            if (s[index] in different_char):
                while (s[index] in different_char):
                    different_char.remove(s[l])
                    l +=1
            different_char.add(s[index])
            max_len = max(max_len, index - l +1)

        return max_len
