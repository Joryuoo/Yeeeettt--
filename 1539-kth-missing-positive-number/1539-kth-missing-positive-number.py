class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2
            miss = (arr[mid] - 1) - mid

            if miss < k:
                l = mid + 1
            else:
                r = mid

        return l + k