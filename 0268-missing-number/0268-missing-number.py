class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xor = 0

        for i in range(n):
            xor ^= i
            xor ^= nums[i]

        xor ^= n
        return xor