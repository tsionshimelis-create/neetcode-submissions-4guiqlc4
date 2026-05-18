class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0
        count = Counter(tasks)
        queue = deque()
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)

        print(maxHeap)

        while maxHeap or queue:
            cycle += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1 != 0:
                    queue.append([cnt + 1, cycle + n])

            if queue and queue[0][1] == cycle:
                cnt, cyl = queue.popleft()
                heapq.heappush(maxHeap, cnt)

        return cycle
        
        
