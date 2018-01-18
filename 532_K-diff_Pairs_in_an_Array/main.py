class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if (k < 0):
            return 0
        
        res = 0
        exp = {}
        cnt = {}

        for v in nums:
            if (v not in cnt):
                cnt[v] = 1
            else:
                cnt[v] += 1

        for v in nums:
            if (v not in exp):
                exp[v] = 1
                if (k == 0 and cnt[v] > 1):
                    res += 1
                elif (k != 0 and (v+k) in cnt):
                    res += 1
            else:
                continue
        
        return res
