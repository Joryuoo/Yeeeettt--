class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = 0
        j = 0
        sum_ = 0

        while i < len(t):
            if t[i] in s and t[i] == s[j]:
                j += 1
                sum_ += 1
            i += 1
        
        return sum_ == len(s)
