'''
202. Happy Number 
https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number n is "happy". A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly 
in a cycle which does not include 1. Those numbers for which this process ends in 1 are 
happy numbers. Return True if n is a happy number, and False if not.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        nstr = str(n)
        stopStrs = ["0", "1"]
        ones = self.count1s(nstr)
        #print("ones init: ", ones)
        numStore = set([])
        s = 0
        while any(int(x)>=1 for x in nstr):
            numStore.add(s)
            s = 0
            for i in range(len(nstr)):
                s += int(nstr[i])**2
            #print("s= ", s)
            
            if s in numStore:
                return False
            
            nstr = str(s)
            # count number of 1's in nstr
            ones = self.count1s(nstr)
            #print("ones: ", ones)
            
            if ones == 1 and all(x in stopStrs for x in nstr):
                return True
            
        return False
    
    def count1s(self, nstr):
        c = 0
        for x in nstr:
            if x == "1":
                c += 1
        return c

    def test1(self):
        input = 19
        res = self.isHappy(input)
        print("res: ", res)

s = Solution()
s.test1()