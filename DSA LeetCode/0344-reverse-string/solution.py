class Solution:
    def reverseString(self, s: List[str]) -> None:
        reverse = []
        for x in range (len(s)-1, -1, -1):
            reverse.append(s[x]) 
        s.clear()
        s.extend(reverse)
            
        
