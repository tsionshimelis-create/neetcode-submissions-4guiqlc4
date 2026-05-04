class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = {c: [] for c in range(n)}
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(start):
            visited.add(start)
            for neigh in adj[start]:
                if neigh not in visited:
                    dfs(neigh)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
