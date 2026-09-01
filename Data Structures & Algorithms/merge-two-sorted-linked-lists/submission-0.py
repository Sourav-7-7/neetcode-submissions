# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        first=list1
        second=list2
        while first is not None and second is not None:
            if first.val < second.val:
                cur.next=first
                first=first.next
            else:
                cur.next=second
                second=second.next
            cur=cur.next
        if first is not None:
            cur.next=first
        else:
            cur.next=second
        return dummy.next