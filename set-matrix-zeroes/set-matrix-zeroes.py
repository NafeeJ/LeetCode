class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len, col_len = len(matrix), len(matrix[0])
        row, col = False, False
        
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
        
        for i in range(row_len)[1:]:
            if matrix[i][0] == 0:
                for j in range(col_len)[1:]:
                    matrix[i][j] = 0
                    
        for j in range(col_len)[1:]:
            if matrix[0][j] == 0:
                for i in range(row_len)[1:]:
                    matrix[i][j] = 0
                    
        if row:
            for j in range(col_len):
                matrix[0][j] = 0
                
        if col:
            for i in range(row_len):
                matrix[i][0] = 0