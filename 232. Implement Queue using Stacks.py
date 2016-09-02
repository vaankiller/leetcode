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
        self._q.pop()

    def peek(self):
        """
        :rtype: int
        """

    def empty(self):
        """
        :rtype: bool
        """