class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        maxLen = 0
        lstr = {}
        head = 0
        for i in range (len(s)):

            if (s[i] not in lstr):
                lstr[s[i]] = i
                length += 1
                if (length > maxLen):
                    maxLen = length
            else:
                if (lstr[s[i]] < head):
                    lstr[s[i]] = i
                    length += 1
                    if (length > maxLen):
                        maxLen = length                    
                else:
                    length = length - (lstr[s[i]]-head)
                    head = lstr[s[i]]+1
                    lstr[s[i]] = i

        return maxLen
