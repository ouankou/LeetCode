class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n < 0):
            neg = True
            n = -n
        else:
            neg = False
        
        flip = False
        res = 1
        cur = 0
        step = (x, 1)
        steps = [(1, 0)]
        cnt = 0
        while (cur != n and res != 0):
            if (cur > n):
                flip = True
                cnt -= 1
                res /= steps[cnt][0]
                cur -= steps[cnt][1]
            else:
                if (flip):
                    cnt -= 1
                    res *= steps[cnt][0]
                    cur += steps[cnt][1]
                else:
                    if (cur == 0):
                        res *= x
                        steps.append((x, 1))
                        cur += 1
                    else:
                        res *= res
                        steps.append((res, cur*2))
                        cur *= 2
                    cnt += 1
        
        if (neg and res != 0):
            return 1/res
        else:
            return res
