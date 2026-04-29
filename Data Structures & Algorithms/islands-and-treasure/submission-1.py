class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start):
            queue = deque()
            queue.append([start, 0])
            visited = set()
            visited.add(start)
            while queue:
                node, level = queue.popleft()
                r,c = node
                
                for dr, dc in directions:
                    row, col = r + dr, c +dc
                    if row in range(rows) and col in range(cols) and grid[row][col] != -1:
                        if grid[row][col] > level + 1:
                            grid[row][col] = level + 1
                        if (row, col) not in visited:
                            queue.append([(row, col), level + 1])
                            visited.add((row, col))
            
                        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs((r, c))

