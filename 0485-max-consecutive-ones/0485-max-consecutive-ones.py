class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        zeroFound = False
        max = 0
        ctr = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                ctr += 1

                if zeroFound:
                    zeroFound = False
                if ctr > max:
                    max = ctr
            else:
                zeroFound = True
                ctr = 0
        return max

            
                
                
        