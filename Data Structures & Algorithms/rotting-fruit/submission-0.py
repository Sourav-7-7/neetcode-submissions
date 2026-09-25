class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        fresh=0
        minutes=0
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        while queue:
            old_fresh=fresh
            level_size=len(queue)
            for _ in range(level_size):
                cell=queue.popleft()
                cur_row,cur_column=cell
                for dr,dc in direction:
                    nr=dr+cur_row
                    nc=dc+cur_column
                    if (0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
            if old_fresh > fresh:
                minutes+=1
        if fresh==0:
            return minutes
        else:
            return -1
