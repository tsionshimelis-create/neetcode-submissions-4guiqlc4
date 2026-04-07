class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        _min = [0] * len(height)

        for i in range(len(height)):
            _min[i] = min(maxLeft[i], maxRight[i])
        
        rain = 0

        for i in range(len(height)):
            trapped = _min[i] - height[i]
            if trapped > 0:
                rain += trapped
        return rain