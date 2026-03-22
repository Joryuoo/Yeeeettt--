class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        firstSeen = -1
        lastSeen = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                firstSeen = mid
            if nums[mid] >= target: #leaning towards left
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                lastSeen = mid
            if nums[mid] <= target: #leaning towards right
                l = mid + 1
            else:
                r = mid - 1
        
        return [firstSeen, lastSeen]
        