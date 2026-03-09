class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = s.split()
        last = tokens[len(tokens) - 1]

        return len(last)
        