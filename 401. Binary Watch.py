__author__ = 'vaan'


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        times = []
        ret = []
        if num is None or num < 0 or num > 8:
            return []

        if num == 0:
            return ["0:00"]

        for i in range(0, 12):
            for j in range(0, 6):
                for k in range(0, 10):
                    times.append(str(i)+':'+str(j)+str(k))
        
        for time in times:
            cnt = self.get_lights_cnt(time)
            if cnt == num:
                ret.append(time)
        return ret


    def get_lights_cnt(self, time):
        hour, minute = tuple(time.split(':'))
        hour_cnt = bin(int(hour)).count('1')
        minute_cnt = bin(int(minute)).count('1')
        return hour_cnt + minute_cnt


s = Solution()
s.readBinaryWatch(4)
