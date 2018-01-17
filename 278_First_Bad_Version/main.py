# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 0
        r = n+1
        cur = 1
        bad = -1
        while(cur > l and cur < r and l < r):
            if (isBadVersion(cur)):
                r = cur
                bad = cur
                cur -= max(1, int((r-l+1)/2))
            else:
                l = cur
                cur += max(1, int((r-l+1)/2))

        if (isBadVersion(l) and l < bad):
            return l
        else:
            return bad
