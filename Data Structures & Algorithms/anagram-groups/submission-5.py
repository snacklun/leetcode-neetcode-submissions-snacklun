class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for index in strs:
            string_key = "".join(sorted(index))
            result.setdefault(string_key,[]).append(index)
        
        return list(result.values())
