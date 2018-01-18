class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(M)
        c = len(M[0])
        
        res = [[0 for x in range(c)] for y in range(r)]
        
        def blur(x, y):
            if (x < 0 or x > r-1 or y < 0 or y > c-1):
                return (0, 0)
            else:
                return (M[x][y], 1)
        
        for i in range(r):
            for j in range(c):
                cnt = 1
                total = M[i][j]
                
                tmp = blur(i-1, j-1)
                total += tmp[0]
                cnt += tmp[1]
                tmp = blur(i-1, j)
                total += tmp[0]
                cnt += tmp[1]
                tmp = blur(i-1, j+1)
                total += tmp[0]
                cnt += tmp[1]
                tmp = blur(i, j-1)
                total += tmp[0]
                cnt += tmp[1]                
                tmp = blur(i, j+1)
                total += tmp[0]
                cnt += tmp[1]                
                tmp = blur(i+1, j-1)
                total += tmp[0]
                cnt += tmp[1]                
                tmp = blur(i+1, j)
                total += tmp[0]
                cnt += tmp[1]                
                tmp = blur(i+1, j+1)
                total += tmp[0]
                cnt += tmp[1]                
                
                res[i][j] = int(total/cnt)

        return res
