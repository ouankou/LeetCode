class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        tab = {}
        tab[1] = ['']
        tab[2] = ['a', 'b', 'c']
        tab[3] = ['d', 'e', 'f']
        tab[4] = ['g', 'h', 'i']
        tab[5] = ['j', 'k', 'l']
        tab[6] = ['m', 'n', 'o']
        tab[7] = ['p', 'q', 'r', 's']
        tab[8] = ['t', 'u', 'v']
        tab[9] = ['w', 'x', 'y', 'z']
        tab[0] = ['']
        
        l = len(digits)
        res = ['']
        #work = []
        for i in range (l):
            work = []
            for u in res:
                for v in tab[int(digits[i])]:
                    work.append(u+v)
            res = work[:]
        if (res == ['']):
            return []
        else:
            return res
