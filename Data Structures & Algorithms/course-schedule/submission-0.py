class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # to detect a cycle in a directed graph:
        # check if a node is visited and at the same time it is in the path we are currently exploring

        adj = defaultdict(list)
        visited = defaultdict(int)
        pathVisited = defaultdict(int)

        for u, v in prerequisites:
            adj[v].append(u)

        def dfs(start):
            visited[start] = 1
            pathVisited[start] = 1

            for neigh in adj[start]:
                if not visited[neigh]:
                    if dfs(neigh):
                        return True
                else:
                    if pathVisited[neigh]:
                        return True
            pathVisited[start] = 0
            return False
            
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False

        return True

        