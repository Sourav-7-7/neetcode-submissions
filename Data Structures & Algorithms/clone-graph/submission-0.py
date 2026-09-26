"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if node is None:
            return None
        clone={}
        clone[node]=Node(node.val)
        queue=deque([node])
        while queue:
            cur=queue.popleft()
            cur_clone=clone[cur]
            for neighbor in cur.neighbors:
                if neighbor in clone:
                    cur_clone.neighbors.append(clone[neighbor])
                if neighbor not in clone:
                    neighbor_clone=Node(neighbor.val)
                    clone[neighbor]=neighbor_clone
                    queue.append(neighbor)
                    cur_clone.neighbors.append(clone[neighbor])
        return clone[node]
