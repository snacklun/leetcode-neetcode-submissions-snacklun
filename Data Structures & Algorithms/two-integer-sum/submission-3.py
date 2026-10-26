class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        for index, value in enumerate(nums):
            value_to_find = target - value
            if (value_to_find not in counts):
                counts[value] = index
            else:
                return [counts[value_to_find], index]