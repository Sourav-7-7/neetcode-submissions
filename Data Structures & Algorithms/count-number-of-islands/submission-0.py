class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        island=0
        visited=set()
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and (r,c) not in visited:
                    island+=1
                    queue=deque([(r,c)])
                    visited.add((r,c))
                    while queue:
                        cell=queue.popleft()
                        r,c=cell
                        for dr,dc in directions:
                            nr=dr+r
                            nc=dc+c
                            if ((0 <= nr < len(grid) and 
                            0 <= nc < len(grid[0])) and
                            (grid[nr][nc]=="1") and
                            (nr,nc) not in visited):
                                visited.add((nr,nc))
                                queue.append((nr,nc))
        return island
