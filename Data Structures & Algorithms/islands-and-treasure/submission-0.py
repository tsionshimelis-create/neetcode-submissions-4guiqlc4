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
                r, c = node
                if grid[r][c] == 0:
                    return level
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] != -1:
                        queue.append([(row, col), level + 1])
                        visited.add((row, col))  
                
            return 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs((r, c))

