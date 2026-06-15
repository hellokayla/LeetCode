from copy import deepcopy
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return
    
        r = len(matrix) # rows  4
        c = len(matrix[0]) # columns 5
        cache = [[int(val) for val in row] for row in matrix]
        max_res = 0
        # bottom up solution
        for i in range(0, r):
            for j in range(0, c):
                if (i == 0 or j == 0): # border 
                    pass
                elif int(matrix[i][j]) > 0:
                    cache[i][j] = 1 + min(cache[i][j-1], cache[i-1][j], cache[i-1][j-1])
                if cache[i][j] > max_res:
                    max_res = cache[i][j]
        return max_res*max_res      



    