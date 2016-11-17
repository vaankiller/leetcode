__author__ = 'vaan'


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x is not None:
            self.stack.append(x)
            self.size += 1
            if self.min is None or x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            pop = self.stack.pop(-1)
            self.size -= 1
            if self.size:
                if pop == self.min:
                    self.min = min(self.stack)
            else:
                self.min = None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print param_3, param_4


