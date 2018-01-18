class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAXINT = 2**31 - 1
        res = 0
        neg = False
        if (dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0):
            neg = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        steps = []
        step = (0, 0)
        cnt = 0
        flip = False
        while (dividend >= divisor or dividend < 0):
            if (dividend < 0):
                flip = True
                step = steps[cnt-1]
                cnt -= 1
                dividend += step[0]
                res -= step[1]
            else:
                if (not flip):
                    step = (max(divisor, step[0]+step[0]), max(1, step[1]+step[1]))
                    steps.append(step)
                    cnt += 1
                    dividend -= step[0]
                    res += step[1]
                else:
                    step = steps[cnt-1]
                    cnt -= 1
                    dividend -= step[0]
                    res += step[1]                    
        
        if (neg):
            return max(-res, -MAXINT-1)
        else:
            return min(res, MAXINT)
