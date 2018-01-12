class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ''
        work = []
        cnt = 0
        l = len(s)
        n = 0
        col = 0
        while (l > 0):
            work.append(['']*numRows)
            col += 1
            if (col%2 != 0):
                for i in range(numRows):
                    if (n < len(s)):
                        work[col-1][i] = s[n]
                        n += 1
                        l -= 1
                    else:
                        work[col-1][i] = ''
            else:
                for i in range(numRows):
                    if (i == 0):
                        work[col-1][i] = ''
                    elif (i == numRows-1):
                        work[col-1][i] = ''
                    elif (n < len(s)):
                        work[col-1][numRows-i-1] = s[n]
                        n += 1
                        l -= 1
                    else:
                        work[col-1][numRows-i-1] = ''
            
        
        for i in range (numRows):
            for j in range (len(work)):
                res += work[j][i]
        
        
        return res
