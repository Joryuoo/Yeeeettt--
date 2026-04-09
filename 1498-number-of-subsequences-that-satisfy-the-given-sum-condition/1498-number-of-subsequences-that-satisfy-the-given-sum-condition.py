class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0

        while l <= r:
            res = nums[l] + nums[r]

            if res <= target:
                ans = (ans + 2**(r - l)) % (10**9 + 7) #combinations inside this range
                l += 1
            else:
                r -= 1
        
        return ans