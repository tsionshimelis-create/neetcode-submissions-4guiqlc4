class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        queue = deque()
        visited = set()
        pathVisited = set()
        # valid Tree : no cycle, connected, undirected
        adj = {v:[] for v in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # check if a neighbor has been visited before and if it has check
        # if it is not the parent of the current node or neigh != parent we are in a cycle
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adj[node]:
                
                if neigh == parent:
                    continue
                
                if neigh in visited:
                    return True
                
                if dfs(neigh, node):
                    return True
            
            return False
           




        count = 0
        for i in range(n):
            if i not in visited:
                if dfs(i, -1):
                    return False
                count += 1
        
        if count > 1:
            return False

        return True
                