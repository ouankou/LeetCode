class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        begin = 0
        end = -1
        exp = {}
        
        if (len(S) == 0):
            return []
        else:
            exp[S[0]] = 1
            for i in range (len(S)-1, -1, -1):
                if (S[i] == S[0]):
                    end = i
                    break
        
        for i in range (1, len(S)):
            if (S[i] in exp):
                continue
            else:
                exp[S[i]] = 1
            if (i > end):
                res.append(end-begin+1)
                begin = i
                end = i
            for j in range (len(S)-1, i-1, -1):
                if (S[j] == S[i]):
                    if (j > end):
                        end = j
                    break
        res.append(end-begin+1)
                    
        return res
