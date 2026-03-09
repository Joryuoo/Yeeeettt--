class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        st = ''
        minlen = len(word1)
        maxlen = len(word2)

        if maxlen < minlen:
            minlen, maxlen = maxlen, minlen
        
        i = 0
        while i < minlen:
            st += word1[i] + word2[i]
            i += 1
        
        while i < maxlen:
            if len(word1) > len(word2):
                st += word1[i]
            else:
                st += word2[i]
            i += 1
        return st