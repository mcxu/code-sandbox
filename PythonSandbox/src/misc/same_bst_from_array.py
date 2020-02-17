'''
Same BSTs
Given 2 arrays of integers, each representing a BST if the values from each array
are inserted into a BST. Return whether or not the 2 arrays would construct the
same BST. BST node:  left value < root <= right value

Sample input: [10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]
Sample output: True
'''

class Prob:
    """
    Time complexity: O(n^2): For each value in an array, go through all values at subsequent indices.
    Space complexity: O(n^2): (n calls of sameBsts on the recursion stack) * ( len(sm1)+len(lg1)==n values stored each call)
    """
    @staticmethod
    def sameBsts(arrayOne, arrayTwo):
        print("-----")
        if not arrayOne and not arrayTwo:
            # both empty, balanced
            return True
        elif len(arrayOne) != len(arrayTwo):
            # there exists an imbalance
            return False 
        
        r1 = arrayOne[0]
        r2 = arrayTwo[0]
        
        if r1 != r2:
            return False
        
        sm1 = []; lg1 = []
        for i in range(1, len(arrayOne)):
            v = arrayOne[i]
            if v < r1:
                sm1.append(v)
            else:
                lg1.append(v)
        
        sm2 = []; lg2 = []
        for i in range(1, len(arrayTwo)):
            v = arrayTwo[i]
            if v < r2:
                sm2.append(v)
            else:
                lg2.append(v)
        print("r1: {}, sm1: {}, lg1: {}".format(r1, sm1, lg1))
        print("r2: {}, sm2: {}, lg2: {}".format(r2, sm2, lg2))
        
        smCall = Prob.sameBsts(sm1, sm2) # recursive call for comparing smaller num arrays
        lgCall = Prob.sameBsts(lg1, lg2) # recursive call for comparing larger num arrays
        # since each call must return something, return the 'and' since both smaller and 
        # larger arrays need to return true for the whole "tree" to be a BST.
        return smCall and lgCall 
        
    @staticmethod
    def test1():
        arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        ans = Prob.sameBsts(arrayOne, arrayTwo)
        print("test1: ans: ", ans)
    
    @staticmethod
    def test2():
        # should be False
        arrayOne = [5, 2, -1, 100, 45, 12, 8, -1, 8, 10, 15, 8, 12, 94, 81, 2, -34]
        arrayTwo = [5, 8, 10, 15, 2, 8, 12, 45, 100, 2, 12, 94, 81, -1, -1, -34, 8]
        ans = Prob.sameBsts(arrayOne, arrayTwo)
        print("test2: ans: ", ans)
        
    @staticmethod
    def test3():
        # should be False
        arrayOne = [1, 2, 3, 4, 5, 6, 7, 8]
        arrayTwo = [1, 2, 3, 4, 5, 6, 7]
        ans = Prob.sameBsts(arrayOne, arrayTwo)
        print("test3: ans: ", ans)
        

Prob.test1()
#Prob.test2()
#Prob.test3()

""" Not correct """
#     @staticmethod
#     def sameBsts(arrayOne, arrayTwo):
#         freqMap = {}
#     
#         for i in range(len(arrayOne)):
#             val = arrayOne[i]
#             if val not in freqMap.keys():
#                 freqMap[val] = 1
#             else:
#                 freqMap[val] += 1
#     
#         for i in range(len(arrayTwo)):
#             val = arrayTwo[i]
#             if val not in freqMap.keys():
#                 return False
#             else:
#                 freqMap[val] -= 1
#     
#             if freqMap[val] <= 0:
#                 freqMap.pop(val)
#     
#         if freqMap.keys():
#             return False
#         return True
        