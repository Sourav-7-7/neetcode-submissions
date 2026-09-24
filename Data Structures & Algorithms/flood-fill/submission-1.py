class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        org_col=image[sr][sc]
        if org_col==color:
            return image
        image[sr][sc]=color
        queue=deque([(sr,sc)])
        while queue:
            cell=queue.popleft()
            r,c=cell
            for dr,dc in directions:
                nr= dr + r
                nc= dc + c
                if ((0 <= nr < len(image)) and
                (0 <= nc < len(image[0]))and
                image[nr][nc]==org_col):
                    image[nr][nc]=color
                    queue.append((nr,nc))
        return image