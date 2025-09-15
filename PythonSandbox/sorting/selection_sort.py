"""
Selection sort
"""

class SelectionSort:
    @staticmethod
    def selectionSort(array):
        for i in range(len(array)-1):
            v = array[i]
            #print("partition at: i:{}, v:{}".format(i,v))
            (loInd, loVal) = SelectionSort.findLowestVal(array[i+1:])
            #print("    loInd: {}, loVal: {}".format(loInd+(i+1), loVal))
            if loVal < v: # swap
                array[i] = loVal
                array[loInd+(i+1)] = v
            #print("    array: ", array)
        return array
    
    # find lowest value, also return index
    @staticmethod
    def findLowestVal(array):        
        loVal = array[0] # assume 1st element is lowest initially
        loInd = 0
        for i in range(1, len(array)):
            val = array[i]
            if val < loVal:
                loVal = val
                loInd = i
        return (loInd,loVal)
    
    @staticmethod
    def test_findLowestVal():
        l = [5,7,2,8,3,7,1,6,9,3]
        (ind, val) = SelectionSort.findLowestVal(l)
        print("{}, {}".format(ind,val))

    @staticmethod
    def test_selectionSort():
        l = [5,7,2,8,3,7,1,6,9,3]
        s = SelectionSort.selectionSort(l)
        print(s)


if __name__ == "__main__":
    #SelectionSort.test_findLowestVal()
    SelectionSort.test_selectionSort()
    