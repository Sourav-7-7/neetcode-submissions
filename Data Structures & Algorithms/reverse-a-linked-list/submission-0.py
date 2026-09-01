# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous=None
        cur=head
        while cur is not None:
            save=cur.next
            cur.next=previous
            previous=cur
            cur=save
        return previous
