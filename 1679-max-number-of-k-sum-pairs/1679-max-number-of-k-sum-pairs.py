class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            if nums[l] + nums[r] == k:
                res += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return res