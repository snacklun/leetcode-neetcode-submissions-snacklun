class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        counts = defaultdict(int)
        
        for index, value in enumerate(s):
            counts[value] += 1

        for index, value in enumerate(t):
            counts[value] -= 1

        return all(value == 0 for value in counts.values())