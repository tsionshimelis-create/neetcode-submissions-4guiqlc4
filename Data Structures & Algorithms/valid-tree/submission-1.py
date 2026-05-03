class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree = connected undirected acyclic graph

        adj_list = {i:[] for i in range(n)}
        visited = set()
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def detectCycle(start, parent):
            
            visited.add(start)
            for neigh in adj_list[start]:
                if neigh not in visited:
                    if detectCycle(neigh, start):
                        return True
                else:
                    if neigh != parent:
                        return True
                

            return False
        

        for i in range(n):
            if i not in visited:
                cycle = detectCycle(i, -1)
                if cycle:
                    return False
                if len(visited) < n:
                    return False

        return True