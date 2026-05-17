from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            x, y = points[i]
            dist = sqrt(x ** 2 + y ** 2)

            heapq.heappush(heap, [-dist, points[i]])
            if len(heap) > k:
                heapq.heappop(heap)

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res