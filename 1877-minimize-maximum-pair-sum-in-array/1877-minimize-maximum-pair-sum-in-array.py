class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        l, r = 0, len(nums) - 1
        mx = 0

        while l < r:
            val = nums[l] + nums[r]

            mx = max(mx, val)
            l+= 1
            r -= 1
        return mx
        