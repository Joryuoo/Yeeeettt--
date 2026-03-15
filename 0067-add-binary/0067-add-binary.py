class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res = ''
        
        a = a[::-1]
        b = b[::-1]
        carry = 0
        i = 0
        while i < max(len(a), len(b)) or carry:
            na = int(a[i]) if i < len(a) else 0
            nb = int(b[i]) if i < len(b) else 0

            val = na + nb + carry

            if val > 2:
                carry = 1
                val = 1
            elif val == 2:
                carry = 1
                val = 0
            else:
                carry = 0
            res += str(val)
            i += 1
        return res[::-1]
        

            