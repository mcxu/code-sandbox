'''
Find kth smallest/largest element in unsorted array

Sample input: [7, 10, 4, 3, 20, 15], k=3, find kth smallest
Sample output: 7

Sample input: [7, 10, 4, 3, 20, 15], k=4, find kth smallest
Sample output: 10

https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
'''

class Prob:
    '''
    smallest = True means kths smallest, if smallest = False, then kth largest
    This method works for arrays containing only positive integers.
    '''
    @staticmethod
    def kthSmLg(array, k, smallest=True):
        # O(m) time, O(m) space, where m = max(array)
        aux = [None for _ in range(max(array)+1)] 
        
        # O(n) time
        for i in range(len(array)):
            val = array[i]
            if aux[val] != None:
                aux[val] += 1
            else:
                aux[val] = 1
        print("aux filled: ", aux)
        
        c = 0 
        i = 0
        if smallest == True:
            while c < k: # O(m) time
                if aux[i] != None:
                    c += aux[i]
                i += 1
            return i-1
        
        else:
            i = len(aux)-1
            while c < k: # O(m) time
                if aux[i] != None:
                    c += aux[i]
                i -= 1
            return i+1
 
    @staticmethod
    def test1():
        array = [7, 10, 4, 3, 20, 15]
        k = 3
        ans = Prob.kthSmLg(array, k, smallest=True)
        print("test1 k={}, ans: {}".format(k, ans))

    @staticmethod
    def test2():
        array = [7, 10, 7, 3, 20, 15]
        k = 6
        ans = Prob.kthSmLg(array, k, smallest=False)
        print("test2 k={}, ans: {}".format(k, ans))

    # ----------------------------------------------------------
    
    '''
    Avg time complexity: O(nlogn)
    '''
    @staticmethod
    def kthLargestQuickselect(array, k):
        # like the quicksort partition
        def partition(array, lowerInd, upperInd):
            pivotElt = array[upperInd]
            print("pivotElt: ", pivotElt)
            i = lowerInd
            j = lowerInd # partition index
            while i <= upperInd:
                print("i=", i)
                if array[i] <= pivotElt:
                    print('array[i]: {}, pivotElt: {}'.format(array[i], pivotElt))
                    # increasing order
                    array[i],array[j] = array[j],array[i]
                    print("swap: {} with {}".format(array[i], array[j]))
                    j += 1
                i += 1
            return j-1 # partition index
        
        def quickSelect(array, lowerInd, upperInd, k):
            if lowerInd < upperInd:
                print("--- lowerInd: {}, upperInd: {}".format(lowerInd, upperInd))
                print("array before partition: ", array)
                partitionIdx = partition(array, lowerInd, upperInd)
                print("array after partition: ", array)
                print("partitionIdx: ", partitionIdx)
                
                if partitionIdx == len(array)-k:
                    return array[partitionIdx]

                if partitionIdx > len(array)-k:
                    return quickSelect(array, lowerInd, partitionIdx-1, k)
                    
                if partitionIdx < len(array)-k:
                    return quickSelect(array, partitionIdx+1, upperInd, k)
            
            # this means that lowerInd == upperInd
            return array[lowerInd]
                
        lowerInd = 0
        upperInd = len(array)-1
        kth = quickSelect(array, lowerInd, upperInd, k)
        return kth
    
    @staticmethod
    def test3():
        #array = [8,4,7,10,3,6,9,2,5,1]
        #array = [6,5,4,3,2,1]
        #array = [3,1,7,4,9,2]
        #array = [5,7,2,3,4,1,6]
        array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        k = 3
        res = Prob.kthLargestQuickselect(array, k)
        print("test3 res: ", res)

    # ----------------------------------------------------------
    
    '''
    If it's ok to mutate original array.
    Time complexity: O(k*len(arr))
    Space complexity: O(1)
    '''
    @staticmethod
    def kthFromMin(arr, k):
        for _ in range(k):
            minimum = float('inf')
            minInd = 0
            for i in range(len(arr)):
                val = arr[i]
                if val < minimum:
                    minimum = val
                    minInd = i
            arr.pop(minInd) 
        return minimum
    
    '''
    Does not mutate original array.
    Time complexity: O(k*len(arr))
    Space complexity: O(len(arr))
    '''
    @staticmethod
    def kthFromMinNonEdit(arr, k):
        # 1 means valid to evaluate. 0 means already previously picked, so dont evaluate again.
        aux = [1 for _ in arr]
        for _ in range(k):
            minimum = float('inf')
            minInd = 0
            for i in range(len(arr)):
                val = arr[i]
                if val < minimum and aux[i] == 1:
                    minimum = val
                    minInd = i
            
            aux[minInd] = 0
        return minimum

    @staticmethod
    def test4():
        a = [3,7,10,9,2,5,11,-1]
        k = int(len(a)/2)
        print("a: {}, k= {}".format(a,k))
        m = Prob.kthFromMinNonEdit(a, k)
        print("a after:", a)
        print(m)
    
#Prob.test1()
#Prob.test2()
Prob.test3()
#Prob.test4()
