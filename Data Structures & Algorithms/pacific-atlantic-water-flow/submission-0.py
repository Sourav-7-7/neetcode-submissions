class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r,c,ocean):
            ocean.add((r,c))
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr < 0 or nr >= rows or nc < 0 or nc >=cols:
                    continue
                if (nr,nc) in ocean:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr,nc,ocean)

        pacific=set()
        atlantic=set()
        rows=len(heights)
        cols=len(heights[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        res=[]
        # Pacific borders
        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)
        # Atlantic borders
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        for r in range(rows):
            dfs(r,cols-1,atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
        
