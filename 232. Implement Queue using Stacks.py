__author__ = 'vaan'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._q.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self._q:
            self._q.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if self._q:
            return self._q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return False if self._q else True


q = Queue()
print q.empty()
