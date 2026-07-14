class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for index in range(len(nums)):
            if (nums[index] not in nums_set):
                nums_set.add(nums[index])
            else:
                return True
        
        return False