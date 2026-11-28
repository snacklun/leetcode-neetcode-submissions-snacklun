# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, index, head))
        # TODO: Merge all nodes into one sorted linked list.
        dummy = ListNode(0, None)
        tail = dummy
        while heap:
            value, index, nodeAdd = heapq.heappop(heap)
            tail.next = nodeAdd
            if nodeAdd.next:
                heapq.heappush(heap, (nodeAdd.next.val, index, nodeAdd.next))
            tail = nodeAdd

        # TODO: Return the merged list's head.
        return dummy.next
