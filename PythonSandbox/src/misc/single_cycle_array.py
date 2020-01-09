'''
Single Cycle Array

In a given array, each value is the number of index steps forward or backward.
An array is a "single cycle" array if, starting from any chosen array value,
each other value is visited exactly once.

Sample input: [2,3,1,-4,-4,2]
Sample output: True
'''

class SC:
    @staticmethod
    def hasSingleCycle(array):
        
        for i in range(len(array)):
            visited = [False for val in array]
            print("visited initialized: ", visited)
            
            startVal = array[i]
            print("*** i= %s, startVal: %s" % (i,startVal))
            
            # check for single cycle from each number
            deltaInd = i + startVal
            val = 0
            j = 0
            while j < len(array):
                print("j= {}, deltaInd: {}".format(j,deltaInd))

                deltaInd = deltaInd + val
                print("    deltaInd set to: ", deltaInd)
                
                if deltaInd >= len(array):
                    deltaInd = deltaInd % len(array)
                    print("    (A) deltaInd changed to: ", deltaInd)
                    
                if deltaInd < 0:
                    deltaInd = len(array) + deltaInd
                    print("    (B) deltaInd changed to: ", deltaInd)
                
                val = array[deltaInd]
                print("    val: ", val)
                
                visited[deltaInd] = True
                print("    visited: ", visited)
                
                j+=1
            
            if False in visited:
                return False
        
        return True
        
    
    @staticmethod
    def test1():
        array = [2,3,1,-4,-4,2]
        ans = SC.hasSingleCycle(array)
        print("test1: ans: ", ans)


SC.test1()