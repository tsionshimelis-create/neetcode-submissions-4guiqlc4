class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = {c: [] for c in range(n)}
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(start):
            queue = deque([start])
            visited.add(start)

            while queue:
                node = queue.popleft()
                for neigh in adj[node]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)

            
            
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1

        return count
