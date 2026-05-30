class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if (len(nums) == 0 or k <= 1):
            return 0
        ans = 0
        l = r = 0
        curr = 1
        for index in range(len(nums)):
            curr *= nums[index]
            while curr >= k :
                curr /= nums[l]
                l += 1
            ans = ans + (index - l + 1)
        
        return ans
