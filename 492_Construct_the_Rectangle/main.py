class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        for i in range (int(area**(1/2.0)), -1, -1):
            if (area%i == 0):
                return (area/i, i)
            
        return None
