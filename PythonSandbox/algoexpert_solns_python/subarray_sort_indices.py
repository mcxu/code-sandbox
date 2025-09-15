'''
Subarray Sort Indices

Given array of integers, return [start,end] indices of 
the smallest subarray that must be sorted in order for the 
entire array to be sorted. Input array length >= 2. If array
is already sorted return [-1,-1].

Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample output: [3, 9]
'''

class Prob:
    @staticmethod
    def subarraySort(array):
        aux = []
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                aux.append((i,array[i]))
        for i in range(len(array)-2, -1, -1):
            if array[i] > array[i+1]:
                aux.append((i,array[i]))
        print("aux: ", aux)
              
        if not aux:
            return [-1,-1]
        
        maxTup = max(aux, key = lambda x: x[1])
        minTup = min(aux, key = lambda x: x[1])
        print("minTup: {}, maxTup: {}".format(minTup, maxTup))
        
        minInd, maxInd = 0, len(array)-1
        while array[minInd] <= minTup[1] or array[maxInd] >= maxTup[1]:
            if array[minInd] <= minTup[1]:
                minInd += 1
            if array[maxInd] >= maxTup[1]:
                maxInd -= 1
            
        print("minInd: {}, maxInd: {}".format(minInd, maxInd))
        return [minInd, maxInd]

    @staticmethod
    def test1():
        array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        ans=  Prob.subarraySort(array)

Prob.test1()