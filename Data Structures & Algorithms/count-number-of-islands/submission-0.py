class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0

        def bfs(start):
            nonlocal count

            queue = deque()
            queue.append(start)

            while queue:
                row, col = queue.popleft()
                visited.add((row, col))
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r,c))
            
            count += 1


        



        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs((i, j))

        return count
    