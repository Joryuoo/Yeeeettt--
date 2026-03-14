class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """


        l = 0
        res = float('-inf')
        subres = 0
        for r in range(len(nums)):
            subres += nums[r]

            if (r - l + 1) > k:
                subres -= nums[l]
                l += 1

            if (r - l + 1) == k:
                res = max(subres, res)
                
        return res / float(k)