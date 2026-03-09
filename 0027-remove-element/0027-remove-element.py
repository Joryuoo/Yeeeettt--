class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        unique, j = 0, 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[unique] = nums[j]
                unique += 1

            j += 1
        return unique
            
                
        