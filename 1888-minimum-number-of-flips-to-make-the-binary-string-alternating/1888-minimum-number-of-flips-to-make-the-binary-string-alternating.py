class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        #type1
        s = s + s
        #type2
        bin0 = bin1 = ''
        res = len(s)
        dif1 = dif2 = 0

        for i in range(len(s)):
            bin1 += '0' if i % 2 else '1'
            bin0 += '1' if i % 2 else '0'
        
        l = 0
        
        for r in range(len(s)):
            if s[r] != bin1[r]:
                dif1 += 1
            if s[r] != bin0[r]:
                dif2 += 1
                
            if (r - l + 1) > n: #ni exceed na sa window
                if s[l] != bin1[l]:
                    dif1 -= 1
                if s[l] != bin0[l]:
                    dif2 -= 1
                l += 1
            
            if (r - l + 1) == n: #whole window
                res = min(dif1, dif2, res)

            

        return res
        