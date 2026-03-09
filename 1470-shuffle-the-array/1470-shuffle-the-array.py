class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        ans, x, y = [0] * (2 * n), 0, 0
        for i in range(n * 2):
            if i % 2 == 0:
                ans[i] = nums[x]
                x += 1
            else:
                ans[i] = nums[n + y]
                y += 1

                
        
        return ans