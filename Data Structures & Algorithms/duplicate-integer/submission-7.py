class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setChars = set()
        for x in nums:
            if x in setChars:
                return True
            else:
                setChars.add(x)
        return False
        