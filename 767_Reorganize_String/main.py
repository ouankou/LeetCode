class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        cnt = []
        for c, n in sorted((S.count(v), v) for v in set(S)):
            if (2*c-1 > len(S)):
                return ''
            cnt.extend(n*c)
        
        res = ['']*len(S)
        res[::2] = cnt[len(S)/2:]
        res[1::2] = cnt[:len(S)/2]
        
        return ''.join(res)
