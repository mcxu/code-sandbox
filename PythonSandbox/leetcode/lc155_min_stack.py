import sys

class MinStack:

    def __init__(self):
        self.stack = [] # last is top
        self.minVals = [] # also a stack, but only stores min vals, last is top

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals or val <= self.minVals[-1]:
            self.minVals.append(val)

    def pop(self) -> None:
        poppedVal = self.stack.pop(-1)
        if self.minVals and poppedVal <= self.minVals[-1]:
            self.minVals.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minVals:
            return self.minVals[-1]

        return -sys.maxsize-1