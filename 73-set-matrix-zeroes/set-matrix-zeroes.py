class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows=set()
        zero_cols=set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        print(zero_rows)
        print(zero_cols)
        
        for r in zero_rows:
            matrix[r]=[0]*cols

        for c in zero_cols:
          for r in range(rows):
            matrix[r][c] = 0
        
        return matrix