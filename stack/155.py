class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        print(f'top: {self.stack[-1]}')
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        print(f'min: {min(self.stack)}')
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.getMin() # returns -3
    obj.pop()
    obj.top()    # returns 0
    obj.getMin() # returns -2