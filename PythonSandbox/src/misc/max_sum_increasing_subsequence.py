'''
Max sum increasing subsequence

Given array of integers, return an array of length 2 of the following:
[    Max possible sum given by a subsequence of increasing values,
    [The sequence of increasing values]
]

Sample input: [10, 70, 20, 30, 50, 11, 30]
Sample output: [110, [10, 20, 30, 50]]
'''
class Prob:
    @staticmethod
    def maxSumIncreasingSubsequence(array):
        maxSumUpToVal = [n for n in array]
        maxSumValues = []
        maxSumOverall = -float('inf')
        maxValuesOverall = []
        
        for i in range(len(array)):
            print("---")
            print("array: ", array)
            inputVal = array[i]
            maxSumValues.clear()
            
            for j in range(0, i):
                print("ival={}, jval={}".format(array[i],array[j]))
                upToVal = array[j]
                if upToVal < inputVal and inputVal + maxSumUpToVal[j] > maxSumUpToVal[i]:
                    print("A")
                    maxSumUpToVal[i] = inputVal + maxSumUpToVal[j]
                    maxSumValues.append(upToVal)
            
            maxSumValues.append(inputVal)
            
            if maxSumUpToVal[i] > maxSumOverall:
                print("B. maxSumUpToVal: {}".format(maxSumUpToVal[i]))
                maxSumOverall = maxSumUpToVal[i]
                maxValuesOverall = maxSumValues.copy()
                    
            print("maxSumUpToVal: ", maxSumUpToVal)
            print("maxSumValues: ", maxSumValues)
            print("maxSumOverall: ", maxSumOverall)
            print("maxValuesOverall: ", maxValuesOverall)
        return [maxSumOverall, maxValuesOverall]
                
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
        
    @staticmethod
    def test4():
        array = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50] # correct: [164, [10, 11, 14, 23, 25, 31, 50]
        ans = Prob.maxSumIncreasingSubsequence(array)
        print("test4: ans: ", ans)
        
        
#Prob.test1()
#Prob.test2()
#Prob.test3()
Prob.test4()
