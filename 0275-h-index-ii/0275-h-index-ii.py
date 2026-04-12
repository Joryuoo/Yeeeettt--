class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n - 1
        h = 0

        while l <= r:
            mid = (l + r) // 2

            if citations[mid] >= (n - mid):
                h = n - mid
                r = mid - 1
            else:
                l = mid + 1
        return h
            