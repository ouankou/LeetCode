class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        exp = {}
        res = 0
        
        def probe(x, y):
            if ((x, y) in exp or x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1):
                return 0
            else:
                exp[(x, y)] = 1
            if (grid[x][y] == 0):
                return 0
            else:
                ans = 1
                ans += probe(x-1, y)
                ans += probe(x+1, y)
                ans += probe(x, y-1)
                ans += probe(x, y+1)
            return ans
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, probe(i, j))
        
        return res
