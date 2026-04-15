class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [0] * n
        right = [0] * n
        l = 1
        r = 1

        for i in range(len(nums)):
            j = -i - 1 
            left[i] = l
            right[j] = r
            l *= nums[i]
            r *= nums[j]

        for i in range(n):
            nums[i] = left[i] * right[i]

        return nums

        