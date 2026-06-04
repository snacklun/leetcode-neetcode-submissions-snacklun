class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l  = 0
        current_number = 0
        maximum_length = 0
        for r in range(len(nums)):
           if nums[r] == 0:
               current_number +=1
           while current_number > k:
                if nums[l] == 0:
                   current_number -= 1
                l += 1
           maximum_length = max(maximum_length, r - l + 1)
        return maximum_length
               
