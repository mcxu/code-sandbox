
class Stack:
    def __init__(self):
        self.stackarr = []
    
    def push(self, n):
        nint = n
        if isinstance(n, str):
            nint = int(n)
        self.stackarr.append(nint)
       
    def pop(self):
        count = 0
        while self.stackarr:
            poppedNum = self.stackarr.pop()
            if count % 2 == 0:
                print(poppedNum)
            count += 1


s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)

s.push(10)
s.push(-2)
s.push(3)
s.push(4)

print("stack after push: ", s.stackarr)

s.pop()
