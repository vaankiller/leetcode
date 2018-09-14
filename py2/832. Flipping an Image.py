class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for line in A:
            line[:] = line[::-1]
            for i in range(len(line)):
                line[i] = abs(line[i] - 1)
        return A

