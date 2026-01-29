class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxNumber = 0
        for x in nums:
            if x == 1:
                count += 1
                if count > maxNumber:
                    maxNumber = count
            else:
                count = 0
        return maxNumber
