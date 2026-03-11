class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        count = 0
        for i in range(len(flowerbed)):
            l = 0 if i == 0 else i - 1
            r = i + 1 if i < len(flowerbed) - 1 else len(flowerbed) - 1
            if not flowerbed[l] and not flowerbed[r] and not flowerbed[i]:
                count += 1
                flowerbed[i] = 1
            
        return n <= count

            