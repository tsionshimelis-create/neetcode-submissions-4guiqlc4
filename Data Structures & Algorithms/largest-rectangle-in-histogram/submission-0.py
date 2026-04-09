class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # monotonically increasing stack

        maxArea = 0
        #stores starting position, height
        stack = []
        for i in range(len(heights)):
            idx = i
            while stack and stack[-1][1] > heights[i]:
                elem = stack.pop()
                idx = elem[0]
                height = elem[1]
                maxArea = max((i - idx)*height, maxArea)
            
            stack.append([idx, heights[i]])

        n = len(heights)
        for i in range(len(stack)):
            maxArea = max((n - stack[i][0]) * stack[i][1], maxArea)
        
        return maxArea