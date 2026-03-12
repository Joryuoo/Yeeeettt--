class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        token = s.split()
        token.reverse()
        return " ".join(token)
        