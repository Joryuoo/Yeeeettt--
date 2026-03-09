class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        l1, l2 = len(str1), len(str2)

        for i in range(min(l1, l2), 0, -1):
            if l1 % i > 0 or l2 % i > 0:
                continue
            else:
                fac1 = l1 // i
                fac2 = l2 // i 

                if str1[:i] * fac1 == str1 and str1[:i] * fac2 == str2:
                    return str1[:i]
        return ''

        