class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = 'aeiou'
        l = 0
        r = len(s) - 1
        res  = list(s)

        while l < r:
            if res[l].lower() in vowels and res[r].lower() in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            elif res[l].lower() not in vowels and res[r].lower() in vowels:
                l += 1
            elif res[l].lower() in vowels and res[r].lower() not in vowels:
                r -= 1
            else:
                l += 1
                r -= 1
        return ''.join(res)

        