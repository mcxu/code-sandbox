"""
Write a function that takes in an array of integers and returns a sorted array 
of the three largest integers in the input array. Note that the function should return duplicate integers 
if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
"""

from utils.sorting_utils import SortingUtils
from utils.number_utils import NumberUtils

class ThreeLargestNums:
    @staticmethod
    def threeLargestNums(array):
        # isolate negatives
        negs, poss = NumberUtils.isolateNegatives(array)
        #print("negs: {}\nposs:{}".format(negs, poss))
        negsSorted = ThreeLargestNums.sortNegatives(negs)
        #print("negsSorted:", negsSorted)
        possSorted = SortingUtils.countingSort(poss)
        array = negsSorted + possSorted
        return array[-3:]
        
    @staticmethod
    def sortNegatives(array):
        a = [abs(x) for x in array]
        sa = SortingUtils.countingSort(a)
        array = []
        for x in sa:
            array.insert(0, -x)
        return array

    #all positives
    @staticmethod
    def test_threeLargestNums1():
        a = [10, 5, 9, 10, 12]
        result = ThreeLargestNums.threeLargestNums(a)
        print("result: ", result)
    
    @staticmethod
    def test_sortNegatives():
        a = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7]
        result = ThreeLargestNums.sortNegatives(a)
        print("test_sortNegatives:", result)
        
    @staticmethod
    def test_isolateNegatives():
        a = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
        result = NumberUtils.isolateNegatives(a)
        print("test_isolateNegatives:", result)
    
    # positives and negatives
    @staticmethod
    def test_threeLargestNums2():
        a = [-1, -2, -3, -7, -17, 56,3,2,4,3,2,12,-27, -18, -541, -8, -7, 7]
        result = ThreeLargestNums.threeLargestNums(a)
        print("result: ", result)
        
    @staticmethod
    def test_threeLargestNums3():
        a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        result = ThreeLargestNums.threeLargestNums(a)
        print("result: ", result)

if __name__ == "__main__":
    #ThreeLargestNums.test_isolateNegatives()
    #ThreeLargestNums.test_sortNegatives()    
    #ThreeLargestNums.test_threeLargestNums2()
    ThreeLargestNums.test_threeLargestNums3()
       
    
        