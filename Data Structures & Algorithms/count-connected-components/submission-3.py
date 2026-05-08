class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {c: [] for c in range(n)}
        count = 0
        queue = deque()
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node in visited:
                return
                
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)
            

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
