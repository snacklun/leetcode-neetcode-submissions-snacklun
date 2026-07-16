class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []
        
        for num, freg in count.items():
            if (len(min_heap) < k):
                heapq.heappush(min_heap, (freg,num))
            else:
                temp = min_heap[0][0]
                if (freg > temp):
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freg,num))
                
        return [pair[1] for pair in min_heap]
