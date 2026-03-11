class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maxelem = max(candies)
        res = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxelem:
                res[i] = True
        
        return res
        