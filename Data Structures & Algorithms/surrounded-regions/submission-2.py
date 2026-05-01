class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        # mark zeros that are conneced to a border zero
        visited = [[False] * cols for i in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        def bfs(r, c, visited):
            if board[r][c] != "O":
                return 
            queue = deque()
            queue.append([r,c])
            visited[r][c] = True
            while queue:
                cr, cc = queue.popleft()
                if board[cr][cc] == "O":
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                            queue.append([nr, nc])
                            visited[nr][nc] = True



        for c in range(cols):
            # first row
            bfs(0, c, visited)
            # last row
            bfs(rows - 1, c, visited)
        
        for r in range(rows):
            # first col
            bfs(r, 0, visited)
            # last col
            bfs(r, cols - 1, visited)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"










