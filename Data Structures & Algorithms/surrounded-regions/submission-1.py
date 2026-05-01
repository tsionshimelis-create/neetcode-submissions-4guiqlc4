class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # iterate through the four borders 
        # when we find a zero on the border do a dfs/bfs on it 
        # mark the zeros it can reach as #
        # after we're done iterate through the board and change the # back to zeros

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        queue = deque()

        def bfs():
        
            while queue:
                cr, cc = queue.popleft()
                if board[cr][cc] == "O":
                    board[cr][cc] = "#"
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            queue.append([nr, nc])


        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or 
                c == cols - 1) and board[r][c] == "O":
                    queue.append([r, c])
        bfs()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

    