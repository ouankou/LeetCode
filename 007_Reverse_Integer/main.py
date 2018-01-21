class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        neg = False
        if (x < 0):
            neg = True
            snum = str(-x)
        else:
            snum = str(x)
        
        snum = int(snum[::-1])
        if (neg):
            snum = -snum
        
        if (snum < -2**31 or snum > 2**31-1):
            return 0
        else:
            return snum
