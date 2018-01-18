class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (len(s) == 0):
            return ''
        res = 1
        ans = s[0]
        cur = 1
        l = len(s)
        for i in range (l):
            step = 1
            cur = 1
            #check 'aba'
            while (i - step >= 0 and i + step < l and s[i-step] == s[i+step]):
                cur += 2
                step += 1
            if (cur > res):
                ans = s[i-step+1:i+step]
            res = max(cur, res)
            step = 1
            cur = 0
            #check 'aa'
            while (i + 1 - step >= 0 and i + step < l and s[i+1-step] == s[i+step]):
                cur += 2
                step += 1
            if (cur > res):
                ans = s[i-step+2:i+step]
            res = max(cur, res)
        return ans
