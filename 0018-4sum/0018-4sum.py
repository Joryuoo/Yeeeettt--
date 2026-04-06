class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        size = len(nums)
        nums.sort()
        res = []

        for i in range(size):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, size):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                
                l = j + 1
                r  = size - 1

                while l < r:
                    val = nums[i] + nums[j] + nums[l] + nums[r]

                    if val == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif val < target:
                        l += 1
                    else:
                        r -= 1
        return res

            
