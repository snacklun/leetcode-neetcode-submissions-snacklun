# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        #fast go n+1 node
        for i in range(n+1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        # TODO: Update links, including the case where the head is removed.

        slow.next = slow.next.next

        # TODO: Return the resulting head.
        return dummy.next