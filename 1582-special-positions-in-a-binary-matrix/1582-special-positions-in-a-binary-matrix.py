class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        row, col, special = len(mat), len(mat[0]), 0

        rowChecker = [0] * row
        colChecker = [0] * col
       
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    rowChecker[i] += 1
                    colChecker[j] += 1

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1 and rowChecker[i] == 1 and colChecker[j] == 1:
                    special += 1

        return special
    