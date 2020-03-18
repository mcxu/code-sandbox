"""
Insertion Sort
"""
from utils.number_utils import NumberUtils

class InsertionSort:
    @staticmethod
    def insertionSort(array):
        for i in range(0, len(array)):
            key = array[i]
            j = i-1
            #print("key:{}, i:{} j:{}: array:{}".format(key,i, j,array))
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                array[j] = key
                #print("    i={}, j={}, array:{}".format(i,j, array))
                j -= 1
        return array
            
    @staticmethod
    def test_insertionSort():
        a = [5,3,2,4,1]
        s = InsertionSort.insertionSort(a)
        print("s:", s)

    @staticmethod
    def test_insertionSort2():
        a = NumberUtils.generateRandomNumbers(0, 100, 50, allowDuplicates=True)
        s = InsertionSort.insertionSort(a)
        print("s:", s)

if __name__ == "__main__":
    #InsertionSort.test_insertionSort()
    InsertionSort.test_insertionSort2()