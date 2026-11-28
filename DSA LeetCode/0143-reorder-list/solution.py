# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head is None or head.next is None:
            return

        # TODO: Find the midpoint using slow and fast pointers.
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        # TODO: Split into two separate halves. 
        head2 = slow.next
        
        #1 list
        slow.next = None

        reversePtr = head2
        prevPtr = None
        while reversePtr.next is not None:
            nextPtr = reversePtr.next
            
            reversePtr.next = prevPtr
            prevPtr = reversePtr
            reversePtr = nextPtr
        
        reversePtr.next = prevPtr
        
        # TODO: Reverse the second half.
        #2 reverse list
        head2 = reversePtr
        
        # TODO: Merge the halves by alternating nodes.
        p1 = head
        q2 = head2
        while q2 is not None:
            p1N = p1.next
            q2N = q2.next
            
            p1.next = q2 
            q2.next = p1N

            p1 = p1N
            q2 = q2N
            

        # Modify links in-place; do not change values or return a node.
        return None
        
