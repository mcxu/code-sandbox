# TODO: not finished, need to fix algorithm
class Prob:
    @staticmethod
    def maxSumIncreasingSubsequence(array):
        maxSumUpToValStorage = {} # upToVal: backSum
        maxBackSum = -float('inf')
        maxSumIndices = []
        
        for i in range(len(array)):
            upToVal = array[i]
            print("upToVal: ", upToVal)
            backSum = 0
            backVal = upToVal
            
            backSumIndices = []
            if backVal not in maxSumUpToValStorage.keys():
                for j in range(i, -1, -1):
                    if array[j] <= backVal:
                        backVal = array[j]
                        print(" backVal set to: ", backVal)
                        if backVal + backSum > maxBackSum:
                            backSum += backVal
                        print(" backSum now: ", backSum)
                        backSumIndices.insert(0, j)
                        
                        if backSum > maxBackSum:
                            maxBackSum = backSum
                            maxSumIndices = backSumIndices
                        
                print(" backSum: ", backSum)
                maxSumUpToValStorage[upToVal] = backSum
                

                
        print("maxSumUpToValStorage final: ", maxSumUpToValStorage)
        print("maxSumIndices final: ", maxSumIndices)
        
        return [maxBackSum, [array[i] for i in maxSumIndices]]
                
    @staticmethod
    def test1():
        array = [10, 70, 20, 30, 50, 11, 30]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test1: ans: ", ans)


    @staticmethod
    def test2():
        array = [-1]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test2: ans: ", ans)
        
        
    @staticmethod
    def test3():
        array = [-1, 1] # correct: [1, [1]]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test3: ans: ", ans)
        
        
#Prob.test1()
#Prob.test2()
Prob.test3()