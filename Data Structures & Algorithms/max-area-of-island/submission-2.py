class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        _max = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start, visited):
            
            count = 1
            queue = deque()
            queue.append(start)
            visited.add(start)
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r,c))
                        visited.add((r, c))
                        count += 1                        
            return count
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    _max = max(_max, bfs((r, c), visited))
        return _max


