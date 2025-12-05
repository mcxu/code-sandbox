class MinStack:
    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals:
            self.minVals.append(val)
        elif self.minVals and val <= self.minVals[-1]:
            self.minVals.append(val)
        # print("after push: ", self.stack, "    minvals: ", self.minVals)

    def pop(self) -> None:
        poppedVal = self.stack.pop()
        if self.minVals and poppedVal == self.minVals[-1]:
            self.minVals.pop()
        # print("after pop: ", self.stack, "    minvals: ", self.minVals)

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minVals[-1] if self.minVals else None
    

def test():
    c = MinStack()
    c.push(0)
    c.push(1)
    c.push(0)
    print("getMin: ", c.getMin())
    print("pop: ", c.pop())
    print("getMin: ", c.getMin())
    print("pop: ", c.pop())
    print("getMin: ", c.getMin())
    print("pop: ", c.pop())

if __name__=="__main__":
    test()
