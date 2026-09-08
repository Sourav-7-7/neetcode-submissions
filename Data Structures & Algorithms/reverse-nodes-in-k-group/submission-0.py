# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        cur=prev.next
        while True:
            fast=cur
            for _ in range(k):
                if fast is None:
                    return dummy.next
                fast=fast.next

            previous=None
            tail=cur
            for _ in range(k):
                save=cur.next
                cur.next=previous
                previous=cur
                cur=save
            prev.next=previous
            tail.next=cur
            prev=tail

