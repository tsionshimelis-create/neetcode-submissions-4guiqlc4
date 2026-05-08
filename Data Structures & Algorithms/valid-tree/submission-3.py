class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        queue = deque()
        visited = set()
        # valid Tree : no cycle, connected, undirected
        adj = {v:[] for v in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # check if a neighbor has been visited before and if it has check
        # if it is not the parent of the current node or neigh != parent we are in a cycle
        def bfs(start):
            queue.append([start, -1])
            visited.add(start)

            while queue:
                node, parent = queue.popleft()
                for neigh in adj[node]:
                    if neigh not in visited:
                        queue.append([neigh, node])
                        visited.add(neigh)
                    else:
                        if neigh != parent:
                            return True



        count = 0
        for i in range(n):
            if i not in visited:
                if bfs(i):
                    return False
                count += 1
        
        if count > 1:
            return False

        return True
                