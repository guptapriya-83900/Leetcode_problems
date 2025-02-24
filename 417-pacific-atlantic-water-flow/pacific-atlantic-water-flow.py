class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pac=[[False] * cols for _ in range(rows)]
        atl=[[False] * cols for _ in range(rows)]

        def bfs(source,ocean):
            q=deque(source)
            while q:
                r,c=q.popleft()
                ocean[r][c]=True

                if r>0 and not ocean[r-1][c] and heights[r-1][c]>=heights[r][c]:
                    q.append((r-1,c))  
                if r<rows-1 and not ocean[r+1][c] and heights[r+1][c]>=heights[r][c]:
                    q.append((r+1,c))
                if c>0 and not ocean[r][c-1] and heights[r][c-1]>=heights[r][c]:
                    q.append((r,c-1))
                if c<cols-1 and not ocean[r][c+1] and heights[r][c+1]>=heights[r][c]:
                    q.append((r,c+1))



        pacific=[]
        atlantic=[]

        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))

        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        
        bfs(pacific,pac)
        bfs(atlantic,atl)

        res=[]

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])

        return res

