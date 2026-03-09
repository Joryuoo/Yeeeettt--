class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        convert = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        rev = s[::-1]
        prev = 0

        for sym in rev:
            if prev  > convert[sym]: # IV (4) -> reverse -> VI -> 5 -1
                res -= convert[sym]
            else:
                res += convert[sym]
            prev = convert[sym]
        return res
                
        
            

        
            
            


        