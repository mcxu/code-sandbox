'''
Single Cycle Array

In a given array, each value is the number of index steps forward or backward.
An array is a "single cycle" array if, starting from any chosen array value,
each other value is visited exactly once.

Sample input: [2,3,1,-4,-4,2]
Sample output: True
'''

class SC:
    
    """
    Note, this performs single cycle check with EACH value.
    Time complexity: O(n^2), since array has n values, and inner while has n iterations.
    Space complexity: O(n), since visits has n values.
    """
    @staticmethod
    def hasSingleCycle(array):
        
        for i in range(len(array)):
            visits = [0 for i in array]
            print("*** len array: ", len(array))
            
            startVal = array[i]
            print("** i= %s, startVal: %s" % (i,startVal))
            
            # check for single cycle from each number
            deltaInd = i
            moveVal = startVal
            j = 0
            while j < len(array):
                print("j= {}, deltaInd: {}, moveVal: {}".format(j,deltaInd, moveVal))
                
                deltaInd = (deltaInd + moveVal) % len(array)
                print("    deltaInd set to: ", deltaInd)
                
                moveVal = array[deltaInd]
                print("    moveVal is now: ", moveVal)
                
                visits[deltaInd] += 1 
                print("    visits: ", visits)
                
                j+=1

            if any(n != 1 for n in visits): return False
        
        return True
        
    
    @staticmethod
    def test1():
        array = [2,3,1,-4,-4,2] # True
        ans = SC.hasSingleCycle(array)
        print("test1: ans: ", ans)
    
    @staticmethod
    def test2():
        array = [10, 11, -6, -23, -2, 3, 88, 908, -26] # True
        ans = SC.hasSingleCycle(array)
        print("test2: ans: ", ans)
        
    @staticmethod
    def test3():
        array = [1, 2, 3, 4, -2, 3, 7, 8, -26] # True
        ans = SC.hasSingleCycle(array)
        print("test3: ans: ", ans)
    
    @staticmethod
    def test4():
        array = [1,-1,1]
        ans = SC.hasSingleCycle(array)
        print("test4: ans: ", ans)
        


#SC.test1()
#SC.test2()
#SC.test3()
SC.test4()
