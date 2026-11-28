class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False

        counts = defaultdict(int)
        for value in s1:
            counts[value] += 1
        
        l = 0
        r = len(s1)

        counts2 = defaultdict(int)
        for r in range(len(s1)):
            counts2[s2[r]] += 1

        if counts == counts2:
            return True

        for r in range(len(s1), len(s2), 1):
            counts2[s2[r]] += 1
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                del counts2[s2[l]]
            l = l + 1
            

            if(counts == counts2):
                return True
        return False