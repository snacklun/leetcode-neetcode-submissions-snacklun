# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
                return list2
        if list2 is None:
                return list1

        dummy = ListNode(0, None)
        tail = dummy
        l1 = list1
        l2 = list2
        while l1 is not None and l2 is not None:
            if (l1.val > l2.val):
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        if (l1 is None):
            tail.next = l2
        else:
            tail.next = l1

        return dummy.next
    