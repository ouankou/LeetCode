class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])
        cnt = {}
        exp = {}
        
        def check(x, y, d):
            if (x < 0 or x > r-1 or y < 0 or y > c-1):
                return True
            else:
                if ((x, y) in exp):
                    return True
                else:
                    exp[(x, y)] = 1
                if (d not in cnt or cnt[d] == matrix[x][y]):
                    cnt[d] = matrix[x][y]
                    prob1 = check(x-1, y, d+1)
                    if (prob1 == False):
                        return False
                    prob2 = check(x, y+1, d+1)
                    if (prob2 == False):
                        return False
                    return True
                else:
                    return False
        
        return check(r-1, 0, 0)
