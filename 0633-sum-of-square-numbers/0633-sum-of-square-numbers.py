import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        a, b = 0, int(c**0.5)

        while a <= b:
            res = a**2 + b**2

            if res == c:
                return True
            elif res < c:
                a += 1
            else:
                b -= 1
        return False