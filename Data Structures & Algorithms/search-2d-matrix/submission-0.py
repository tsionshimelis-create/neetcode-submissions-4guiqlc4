class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])


        for _ in range(row):
            l = 0
            r = col - 1
            if target > matrix[_][r]:
                continue
            # elif _ == 0 and target < matrix[_][l]:
            #     return False
            while l <= r:
                mid = l + (r - l)//2

                if matrix[_][mid] == target:
                    return True
                
                elif matrix[_][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
        