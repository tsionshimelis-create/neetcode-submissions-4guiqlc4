class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top = 0
        bot = ROWS - 1

        while top <= bot:
            mid_row = bot + (top - bot) // 2 
            
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        
        if top > bot:
            return False
        
 
        l = 0
        r = COLS - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[mid_row][mid]:
                r = mid - 1
            elif target > matrix[mid_row][mid]:
                l = mid + 1
            else:
                return True
        return False