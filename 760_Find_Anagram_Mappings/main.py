class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        count = {}
        for i in range (0, len(B)):
            count[B[i]] = i
        res = []
        for v in A:
            res.append(count[v])
        
        return res
