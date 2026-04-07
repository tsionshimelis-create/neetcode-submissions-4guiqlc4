class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0



        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        rain = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1    
                maxLeft = max(maxLeft, height[l])

                rain += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])

                rain += maxRight - height[r]
        return rain
            