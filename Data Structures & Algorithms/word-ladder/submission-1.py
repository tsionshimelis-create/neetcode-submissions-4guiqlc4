class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # do a graph 
        graph = defaultdict(set)
        compare = [beginWord] + wordList
        
        for i in range(len(compare)):

            for j in range(len(compare)):
                n = 0 
                if i == j:
                    continue
                for k in range(len(beginWord)):
                    if compare[i][k] != compare[j][k]:
                        n += 1
                if n <= 1:
                    graph[compare[i]].add(compare[j])
        queue = deque()
        visited = set()
        queue.append([beginWord, 1])
        visited.add(beginWord)

        while queue:
            node, length = queue.popleft()
            if node == endWord:
                return length
            for neigh in graph[node]:
                if neigh not in visited:
                    queue.append([neigh, length + 1])
                    visited.add(neigh)

        return 0