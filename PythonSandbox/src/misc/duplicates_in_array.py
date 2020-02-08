'''
Find 1st duplicate value in list.
Find all values that have duplicates in list.
Find all values that are duplicated n times.
'''

class Prob:
    @staticmethod
    def find1stDuplicate(array):
        auxSet = set([]) # auxilary set to store traversed values
        for value in array:
            if value in auxSet:
                return value
            else:
                auxSet.add(value)
        return -1
    
    @staticmethod
    def test1():
        a1 = [1,2,3,4,5,6,7,8,9,0]
        a2 = [1,2,3,4,5,6,7,3,2,0]
        cases = [a1, a2]
        for case in cases:
            print("case: ", case)
            fd = Prob.find1stDuplicate(case)
            print("fd: ", fd)
    
    @staticmethod
    def findAllDuplicates(array):
        auxSet = set([])
        dups = []
        for value in array:
            if value in auxSet:
                dups.append(value)
            else:
                auxSet.add(value)
        return dups # will return empty if no duplicates
    
    @staticmethod
    def test2():
        a1 = [1,2,3,4,5,6,7,8,9,0]
        a2 = [1,2,3,4,5,6,7,3,2,0]
        cases = [a1, a2]
        for case in cases:
            print("case: ", case)
            fd = Prob.findAllDuplicates(case)
            print("fd: ", fd)
    
    @staticmethod
    def findNduplicates(array, n):
        countList = [0] * (max(array) + 1)
        
        for val in array:
            countList[val] += 1
        
        output = []
        for j in range(len(countList)):
            count = countList[j]
            if count == n:
                output.append(array[j-1])
        return output
        
    @staticmethod
    def test3():
        a1 = [1,2,3,4,5,6,7,8,9,0]
        a2 = [1,2,3,4,5,3,7,3,2,7]
        cases = [a1, a2, a2]
        ns = [2, 2, 3]
        for (case,n) in zip(cases,ns):
            print("case: {}, n: {}".format(case,n))
            fd = Prob.findNduplicates(case, n)
            print("fd: ", fd)
        
#Prob.test1()
#Prob.test2()
Prob.test3()

