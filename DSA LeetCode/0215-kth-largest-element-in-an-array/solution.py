class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num * -1)
        
        for index in range(k-1):
            heapq.heappop(min_heap)
        
        return min_heap[0] * -1

