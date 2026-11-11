class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) , len(matrix[0])

        l, r = 0,( row * col) - 1
        while l<=r:
            m = (l+r)//2
            Mid_i = m//col
            Mid_j = m%col
            if target >matrix[Mid_i][Mid_j]:
                l = m + 1 
            elif target < matrix[Mid_i][Mid_j]:
                r = m - 1   
            else:
                return True
        return False              

        