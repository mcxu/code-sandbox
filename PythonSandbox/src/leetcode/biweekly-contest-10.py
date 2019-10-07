"""
Leetcode biweekly contest 10 (10/5/2019)
"""
from queue import Queue
import time

class BiweeklyContest10Scratch:
    def __init__(self):
        pass
    
    """
    1213. Intersection of 3 sorted arrays
    """
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        numdict = {}
        for a in arr1:
            print("a:{}".format(a))
            numdict[a] = 1
        
        for b in arr2:
            if(b in numdict.keys()):
                numdict[b] += 1
        
        for c in arr3:
            if(c in numdict.keys()):
                numdict[c] += 1
        
        print("numdict: {}".format(numdict))
        
        # check for occurrence of 3
        commons = []
        for key in numdict.keys():
            print("key: {}".format(key))
            occ = numdict[key]
            if(occ == 3):
                commons.append(key)
        
        return sorted(commons)

    """
    5081. Stepping Numbers
    """
    def countSteppingNumbersBruteForce(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sns = []
        for i in range(low, high+1):
            intstr = str(i)
            ndigits = len(intstr)
            #print("intstr:{}, ndigits: {}".format(intstr, ndigits))

            # iterate and see if previous val is 1 less
            isstep = True
            for ind in range(1,ndigits):
                #print("ind={}, val={}".format(ind,intstr[ind]))
                if(abs(int(intstr[ind])-int(intstr[ind-1])) != 1):
                    #print("FALSE")
                    isstep = False
            if(isstep is True):
                sns.append(i)
        return sns

    def test_countSteppingNumbersBruteForce(self):
        num = [10, 20, 30, 40, 100, 1000, 100000, 1000000]
        sns = self.countSteppingNumbersBruteForce(0,num[7])
        print("test_countSteppingNumbers: {}".format(sns))

    def countSteppingNumbersBFS(self, low, high):
        sns = []
        for i in range(0,10):
            #print("===== top of for loop, putting i={} in new queue.".format(i))
            q = [] # queue [first....last]
            q.append(i)
            more = True
            while(more is True):               
                #print("--- queue: {}".format(q))

                val = q.pop(0)
                #print("val: " + str(val))
                #print("sns: {}".format(sns))

                if val > high:
                    #print("more is false now")
                    more = False

                if low <= val <= high and val not in sns:
                    sns.append(val)
                    
                oneDown = val*10 + val%10 - 1
                oneUp = val*10 + val%10 + 1

                if val%10 == 0:
                    q.append(oneUp)
                elif val%10 == 9:
                    q.append(oneDown)
                else:
                    q.append(oneDown)
                    q.append(oneUp)
        return sorted(sns)
            
    def test_countSteppingNumbersBFS(self):
        sns = self.countSteppingNumbersBFS(10, 1000000000)
        print("test_countSteppingNumbersBFS: {}".format(sns))


def main():
    bwc10 = BiweeklyContest10Scratch()
    #bwc10.test_countSteppingNumbersBruteForce()
    bwc10.test_countSteppingNumbersBFS()

main()