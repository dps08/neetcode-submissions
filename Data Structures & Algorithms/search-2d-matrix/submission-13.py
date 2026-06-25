class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f_row, l_row = 0, len(matrix) - 1
        while f_row <= l_row:
            mid_row = (f_row+l_row) // 2
            l_col, r_col = 0, len(matrix[mid_row])-1
            if matrix[mid_row][l_col] <= target <= matrix[mid_row][r_col]:
                while l_col <= r_col:
                    mid_col = (l_col+r_col) // 2
                    if target > matrix[mid_row][mid_col]:
                        l_col = mid_col + 1
                    elif target < matrix[mid_row][mid_col]:
                        r_col = mid_col - 1
                    else:
                        return True
                return False
            elif target > matrix[mid_row][-1]:
                f_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                l_row = mid_row - 1
            else:
                return False
        return False