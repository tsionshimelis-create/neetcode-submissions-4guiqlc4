class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def isValid(r, c, visited, pr,pc):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or heights[r][c] < heights[pr][pc]:
                return False
            return True
        def bfs(start, visited, prevHeight):
            r, c = start
            queue = deque()
            queue.append(start)
            visited.add(start)
            
            while queue:
                
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if isValid(nr, nc, visited, cr, cc):
                        queue.append((nr,nc))
                        visited.add((nr,nc))


        for r in range(rows):
            bfs((r, 0), pac, heights[r][0])
            bfs((r, cols -1), atl, heights[r][cols-1])
        for c in range(cols):
            bfs((0, c), pac, heights[0][c])
            bfs((rows - 1, c), atl, heights[rows - 1][c])
        
        print(pac)
        print(atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])

        return res

        