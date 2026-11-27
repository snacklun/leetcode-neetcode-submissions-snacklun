# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        fastPtr = head
        slowPtr = head
        while fastPtr.next is not None and fastPtr.next.next is not None:
            fastPtr = fastPtr.next.next
            if slowPtr.next is not None:
                slowPtr = slowPtr.next
            if (fastPtr == slowPtr):
                return True

        return False