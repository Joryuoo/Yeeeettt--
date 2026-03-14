class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        if digits[n - 1] < 9:
            digits[n - 1] += 1
            return digits
        else:
            i = n
            while i > 0:
                val = digits[i - 1] + 1
                if(val < 10):
                    digits[i - 1] = val
                    return digits
                digits[i - 1] = 0
                i -= 1
        return [1] + digits