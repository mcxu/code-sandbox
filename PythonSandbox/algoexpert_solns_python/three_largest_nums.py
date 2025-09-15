"""
Write a function that takes in an array of integers and returns a sorted array 
of the three largest integers in the input array. Note that the function should return duplicate integers 
if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
"""

class ThreeLargestNums:
    @staticmethod
    def threeLargestNums(arr):
        k = 3
        lo = 0
        hi = len(arr)-1
        pidx = ThreeLargestNums.quickselect(arr, lo, hi, k)
        print("pidx: ", pidx)
        return arr[pidx:]
    
    @staticmethod
    def quickselect(arr, lo, hi, k):
        if lo < hi:
            partitionIdx = ThreeLargestNums.partition(arr, lo, hi)
            
            if partitionIdx == len(arr)-k:
                return partitionIdx

            if partitionIdx > len(arr)-k:
                return ThreeLargestNums.quickselect(arr, lo, hi-1, k)
            if partitionIdx < len(arr)-k:
                return ThreeLargestNums.quickselect(arr, lo+1, hi, k)
        return lo

    @staticmethod
    def partition(arr, lo, hi):
        i = lo
        j = lo
        pivotElt = arr[hi]
        while i <= hi:
            if arr[i] <= pivotElt:
                arr[i],arr[j] = arr[j],arr[i]
                j += 1
            i += 1
        return j-1

    #all positives
    @staticmethod
    def test_threeLargestNums1():
        a = [10, 5, 9, 10, 12]
        result = ThreeLargestNums.threeLargestNums(a)
        print("result: ", result)
    
    # positives and negatives
    @staticmethod
    def test_threeLargestNums2():
        a = [-1, -2, -3, -7, -17, 56,3,2,4,3,2,12,-27, -18, -541, -8, -7, 7]
        result = ThreeLargestNums.threeLargestNums(a)
        print("result: ", result)
        
    @staticmethod
    def test_threeLargestNums3():
        a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        aSorted = sorted(a)
        print('aSorted: ', aSorted)
        print("a: ", a)
        result = ThreeLargestNums.threeLargestNums(a)
        print("result: ", result)

if __name__ == "__main__":
    #ThreeLargestNums.test_isolateNegatives()
    #ThreeLargestNums.test_sortNegatives()    
    #ThreeLargestNums.test_threeLargestNums2()
    ThreeLargestNums.test_threeLargestNums3()
       
    
        