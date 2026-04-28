class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0


        def dfs(start):
            r, c = start
            rowInbounds= 0 <= r and r < rows
            colInbounds= 0 <= c and c < cols

            if not rowInbounds or not colInbounds:
                return False
            if grid[r][c] == "0":
                return False
            
            grid[r][c] = "0"
            dfs((r - 1, c))
            dfs((r + 1, c))
            dfs((r, c - 1))
            dfs((r, c + 1))

            return True





        for r in range(rows):
            for c in range(cols):
                if dfs((r, c)):
                    count += 1

        return count

