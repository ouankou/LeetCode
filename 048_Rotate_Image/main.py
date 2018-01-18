class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = n = len(matrix)
        r = 0
        while (l > 1):
            temp = matrix[r][r:n-r][:]
            
            for i in range (r, n-r-1):
                matrix[r][n-1-i] = matrix[i][r]
                matrix[i][r] = matrix[n-r-1][i]
                matrix[n-r-1][i] = matrix[n-1-i][n-r-1]
                matrix[n-1-i][n-r-1] = temp[-1-i+r]

            r += 1
            l -= 2
