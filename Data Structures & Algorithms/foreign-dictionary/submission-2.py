class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        n = len(words)
        indegree = {c: 0 for w in words for c in w}
        res = []
        queue = deque()
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            length = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:length] == word2[:length]:
                return ""
            for j in range(length):
                if word1[j] != word2[j]:
                
                    if word2[j] not in adj[word1[j]]:
                        indegree[word2[j]] += 1
                    adj[word1[j]].add(word2[j])

                    break
        print(adj)
        print(indegree)
        for u, v in indegree.items():
            if v == 0:
                queue.append(u)
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        print(res)
        return "".join(res) if len(res) == len(adj) else ""