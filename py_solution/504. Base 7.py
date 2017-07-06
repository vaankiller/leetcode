class Solution(object):
    def convertToBase7(self, num):
        if num < 0: 
            return '-' + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)


def main():
    s = Solution()
    print s.convertToBase7(100)
    print s.convertToBase7(-7)

if __name__ == '__main__':
    main()