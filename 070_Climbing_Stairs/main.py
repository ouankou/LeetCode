class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if (n == 1 or n == 2):
            return n
        
        s1 = 1
        s2 = 2
        
        for i in range (3, n+1):
            res = s2 + s1
            s1 = s2
            s2 = res
        
        return res
