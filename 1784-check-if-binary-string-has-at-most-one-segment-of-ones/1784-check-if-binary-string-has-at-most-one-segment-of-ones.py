class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #valid examples: 1100, 110, 111, 100
        #invalid: 0110, 001, 011, 1101, 1110011 -> denotes to string '01' is invalid

        return not '01' in s
        

        