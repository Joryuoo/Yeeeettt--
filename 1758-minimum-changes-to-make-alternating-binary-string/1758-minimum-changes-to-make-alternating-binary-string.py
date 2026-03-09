class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr, b0, b1 = '0', 0, 0
        for c in s:
            if c == curr:
                b1 += 1
            else:
                b0 += 1
            
            curr = '1' if curr == '0' else '0'
        return min(b0, b1)


        