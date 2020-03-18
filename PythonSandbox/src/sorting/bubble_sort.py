'''
Bubblesort
'''
from utils.number_utils import NumberUtils

class BubbleSort:
    
    @staticmethod
    def bubbleSort(array):
        isSorted = False
        lim = len(array)-1
        while(not isSorted):
            isSorted = True
            for i in range(lim):
                if array[i] > array[i+1]:
                    #swap
                    tmp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = tmp
                    isSorted = False
            lim -= 1 # b/c after 1 pass through the array, the last element is sorted
        return array
    
    @staticmethod
    def test_bubbleSort():
        a = [9,7,8,3,5,1]
        s = BubbleSort.bubbleSort(a)
        print(s)
    
    @staticmethod
    def test_bubbleSort2():
        a = NumberUtils.generateRandomNumbers(0, 10000, 100, allowDuplicates=False)
        s = BubbleSort.bubbleSort(a)
        print(s)

if __name__ == "__main__":
    #BubbleSort.test_bubbleSort()
    BubbleSort.test_bubbleSort2()