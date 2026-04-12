class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {}
        def ways(n):
            if n in mem: return mem[n]
            if n == 1: return 1
            elif n == 2: return 2

            mem[n] = ways(n - 1) + ways(n - 2)
            return mem[n]
        
        return ways(n)