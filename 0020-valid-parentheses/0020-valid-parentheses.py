class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = {
            '{':'}',
            '(':')',
            '[':']'
        }
        stack = []
        for char in s:
            if char in valid:
                stack.append(char)
            else:
                if not stack: return False
                top = stack.pop()
                val = valid.get(top)
                if val == char:
                    continue
                else:
                    return False
                

        return True if not stack else False


        