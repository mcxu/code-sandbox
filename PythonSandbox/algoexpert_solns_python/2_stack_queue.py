'''
Implement queue class that uses 2 stacks to make a queue.
'''

class TwoStackQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(val)
        while self.s2:
            self.s1.append(self.s2.pop())
    
    def dequeue(self):
        if not self.s1:
            return None
        dqVal = self.s1.pop() # dequeued value
        return dqVal

class Prob:
    @staticmethod
    def test1():
        arr = [1,2,3,4]
        q = TwoStackQueue()
        for v in arr:
            print("enqueueing: ", v)
            q.enqueue(v)
        
        for v in range(len(arr)+1):
            dq = q.dequeue()
            print("dequeing: ", dq)
        
        q.enqueue(100)
        q.enqueue(200)
        print(q.dequeue())

Prob.test1()