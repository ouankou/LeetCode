class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        cnt = {}
        res = ['']
        for v in words:
            cnt[v] = 1
        
        def check(word):
            cand = []
            for i in range(26):
                if (word+chr(ord('a')+i) in cnt):
                    cand.append(word+chr(ord('a')+i))
            return cand
        
        while (res != []):
            work = []
            for v in res:
                for u in check(v):
                    work.append(u)
            if (work == []):
                return res[0]
            else:
                res = work
