# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        carry=0
        while l1 is not None or l2 is not None:
            total=0
            digit1=l1.val if l1 else 0
            digit2=l2.val if l2 else 0
            total=digit1 + digit2 + carry
            digit=total % 10
            carry=total // 10
            cur.next=ListNode(digit)
            cur=cur.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        if carry != 0:
            cur.next=ListNode(carry)
        return dummy.next