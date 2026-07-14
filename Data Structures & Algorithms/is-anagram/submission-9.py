class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countA = {}
        countB = {}
        for index in s:
            countA[index] = countA.get(index,0) + 1
        for index in t:
            countB[index] = countB.get(index,0) + 1
        if countA == countB:
            return True
        return False