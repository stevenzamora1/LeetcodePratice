class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if self.minStack[-1] > val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())
