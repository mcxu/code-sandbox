'''
Quick sort
'''

class Prob:
    
    @staticmethod
    def quickSort(array):
        lowerInd = 0
        upperInd = len(array)-1
        Prob.quickSortHelper(array, lowerInd, upperInd)
        return array
    
    @staticmethod
    def quickSortHelper(array, lowerInd, upperInd):
        print("entered quickSortHelper. lowerInd: {}, upperInd: {}".format(lowerInd, upperInd))
        print("array initially: ", array)
        if lowerInd < upperInd:
            # partition index
            pIndex = Prob.partition(array, lowerInd, upperInd)
            print("pIndex returned: ", pIndex)
            if pIndex > lowerInd:
                print("A")
                Prob.quickSortHelper(array, lowerInd, pIndex-1)
            
            if pIndex < upperInd:
                print("B")
                Prob.quickSortHelper(array, pIndex+1, upperInd)
    
    @staticmethod
    def partition(array, lowerInd, upperInd):
        pivotElt = array[upperInd]
        print("pivotElt: ", pivotElt)
        i = lowerInd
        j = lowerInd
        while i <= upperInd:
            print("i={}, j={}".format(i,j))
            if array[i] <= pivotElt:
                Prob.swap(array, i, j)
                j += 1
                print("j incremented to:", j)
            i += 1
        
        # return the partition index
        return j-1
            
    @staticmethod
    def swap(array, i, j): # in place
        print("swap i={} with j={}".format(i,j))
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        print("array after swap: ", array)
    
    @staticmethod
    def test_partition():
        array = [2,3,1,5,4]
        lowerInd = 0
        upperInd = len(array)-1
        partInd = Prob.partition(array, lowerInd, upperInd)
        print("partition index: ", partInd)
    
    @staticmethod
    def test1():
        #array = [2,3,5,1,4]
        array = [8,4,7,10,3,6,9,2,5,1]
        qs = Prob.quickSort(array)
        print("test1: ", qs)
    
    @staticmethod
    def test2():
        # worst case: O(n^2) for already sorted array
        array = [i for i in range(10)]
        qs = Prob.quickSort(array)
        print("test2: ", qs)

#Prob.test_partition()
Prob.test1()
#Prob.test2()
        