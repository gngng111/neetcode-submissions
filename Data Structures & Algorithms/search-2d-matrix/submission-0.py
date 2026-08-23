from bisect import bisect_left, bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_column = [row[0] for row in matrix]
        col_index = bisect_right(first_column, target) - 1
        row = matrix[col_index]
        i = bisect_left(row, target)
        if i < len(row) and row[i] == target:
            return True
        return False
        

        