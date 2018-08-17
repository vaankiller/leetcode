class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._top = None
        self._q1 = []
        self._q2 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._top = x
        q = self._q1 or self._q2
        q.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        q = self._q1 or self._q2
        if not self._q1:
            another = self._q1
        else:
            another = self._q2
        
        while len(q) > 1:
            x = q.pop(0)
            self._top = x
            another.append(x)
        return q.pop()
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self._q1 and self._q2


