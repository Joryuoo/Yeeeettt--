class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        rev, orig = 0, x

        while x > 0:
            n = orig % 10
            rev = (rev * 10) + (x % 10)
            x //= 10
        

        return rev == orig
        