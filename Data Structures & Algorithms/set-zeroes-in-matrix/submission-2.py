class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows , cols = len(matrix), len(matrix[0])
        zeros = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append([r,c])
        
        for i in zeros:
            zero_r , zero_c = i[0],i[1]
            for c in range(cols):
                matrix[zero_r][c] = 0
            for r in range(rows):
                matrix[r][zero_c] = 0

        