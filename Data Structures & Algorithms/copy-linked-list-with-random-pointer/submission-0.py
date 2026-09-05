"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        freq={None:None}
        cur=head
        while cur is not None:
            copy=Node(cur.val)
            freq[cur]=copy
            cur=cur.next
        cur=head
        while cur is not None:
            copy=freq[cur]
            copy.next=freq[cur.next]
            copy.random=freq[cur.random]
            cur=cur.next
        return freq[head]
