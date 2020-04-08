'''
Given an array of integers nums and an integer k,
determine whether there are 2 distinct indices i and j
in the array where nums[i]=nums[j] and the absolute difference
between i and j is less than or equal to k.

Example 1:
nums = [0,1,2,3,5,2] and k = 3
output should be: true

Example 2:
nums = [0,1,2,3,5,2] and k = 2
output should be: false
'''

class Prob:
    @staticmethod
    def containsCloseNums(nums, k):
        indMap = {} # format: num : [index]
        
        # get indices that each num appears on.
        for i in range(len(nums)):
            n = nums[i]
            if n in indMap.keys():
                indMap[n].append(i)
            else:
                indMap[n] = [i]
        
        contains = False
        for key in indMap.keys():
            indicesList = indMap[key]
            if len(indicesList) >= 2:
                for j in range(1, len(indicesList)):
                    absDist = abs(indicesList[j] - indicesList[j-1])
                    if absDist <= k:
                        return True
        
        return contains
        
    @staticmethod
    def test1():
        nums = [0,1,2,3,5,2]
        k = 3 # returns true
        #k = 2 # returns false
        res = Prob.containsCloseNums(nums, k)
        print("test1 res: ", res)
        
    @staticmethod
    def test2():
        nums = [0,1,2,3,5,10,2,20,5,9]
        #k = 3 # returns false
        k = 4 # returns true
        res = Prob.containsCloseNums(nums, k)
        print("test2 res: ", res)

#Prob.test1()
Prob.test2()
