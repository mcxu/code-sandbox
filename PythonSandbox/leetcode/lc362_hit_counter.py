# https://leetcode.com/problems/design-hit-counter/

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        #print("hit: timestamp: {}, q before hit: {}".format(timestamp, self.q))
        while self.q and self.q[0]<=timestamp-300:
            self.q.pop(0)
        self.q.append(timestamp)
        #print("q after hit: ", self.q)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        print("getHits: timestamp:{}, q:{}".format(timestamp, self.q))
        
        if self.q and timestamp > self.q[-1]:
            for i in range(len(self.q)):
                if self.q[i] > timestamp-300:
                    #print("i={}, self.q[i]: {}".format(i, self.q[i]))
                    return len(self.q)-i 
                elif i==len(self.q)-1:
                    return 0
        
        # for case that timestamp = self.q[-1]
        return len(self.q)