class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i+1, j+1]


def main():
    s = Solution()
    print s.twoSum([2,3,4], 6)
    print s.twoSum([-1, 0], -1)

if __name__ == '__main__':
    main()