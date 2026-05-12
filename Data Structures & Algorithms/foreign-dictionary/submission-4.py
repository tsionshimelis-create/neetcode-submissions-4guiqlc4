class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = defaultdict(int)
        queue = deque()
        order = []
        for i in range(len(words) - 1):
            
                word1 = words[i]
                word2 = words[i + 1]
                _min = min(len(word1), len(word2))

                if len(word1) > len(word2) and word1[:_min] == word2[:_min]:
                    return ""

                for j in range(_min):
                    if word1[j] != word2[j]:
                        if word2[j] not in adj[word1[j]]:
                            indegree[word2[j]] += 1
                        adj[word1[j]].add(word2[j])
                        
                        
                        break
     
        for key in adj.keys():
            if indegree[key] == 0:
                queue.append(key)
        print(adj)
        print(indegree)
        while queue:
            char = queue.popleft()
            order.append(char)
            
            for neigh in adj[char]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        print(order)
        if len(order) == len(indegree):
            return "".join(order)
        else:
            return ""