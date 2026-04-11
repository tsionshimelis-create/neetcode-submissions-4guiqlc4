import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def possible(mid):
            time = 0

            for i in piles:
                time += math.ceil(i / mid)

            return time <= h


        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            mid = l + (r - l)//2

            if possible(mid):
                ans = mid
                r = mid - 1
            
            else:
                l = mid + 1

        
        return ans

