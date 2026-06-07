class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_value = 0
        min_value = 0
        for index in range(len(nums)):
            start_value += nums[index]
            min_value = min(min_value, start_value)

        start_value = 1 - min_value
        
        return start_value
