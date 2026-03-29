class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n  = numbers
        l, r = 0, len(n) - 1

        while l <= r:
            if n[l] + n[r] == target:
                return [l + 1, r + 1]
            elif n[l] + n[r] < target:
                l += 1
            else:
                r -= 1
            
        