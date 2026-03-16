class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = 'aeiou'
        l = maxCount = c = 0
        
        for r in range(len(s)):
            if s[r] in vowels:
                c += 1
            
            if (r - l + 1) > k:
                if s[l] in vowels:
                    c -= 1
                l += 1

            if (r - l + 1) == k:
                maxCount = max(maxCount, c)
            
        return maxCount