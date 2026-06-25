class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            L, R = 0, len(matrix[i])-1
            if target > matrix[i][-1]:
                continue
            elif target < matrix[i][0]:
                return False
                
            while L<=R:
                mid = (L+R) // 2
                if target < matrix[i][mid]:
                    R = mid - 1
                elif target > matrix[i][mid]:
                    L = mid + 1
                else:
                    return True
        return False