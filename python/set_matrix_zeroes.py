class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_columns = []
        zero_rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_columns.append(j)
                    zero_rows.append(i)
        for zero_column in zero_columns:
            for row in matrix:
                row[zero_column] = 0
        for zero_row in zero_rows:
            matrix[zero_row] = [0] * len(matrix[0])