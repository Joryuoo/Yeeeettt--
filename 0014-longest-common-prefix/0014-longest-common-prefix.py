class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = len(strs[0])

        for s in strs:
            if len(s) < minlen:
                minlen = len(s)

        for i in range(minlen):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
        
        return strs[0][:minlen]

        