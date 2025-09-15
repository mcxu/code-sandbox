'''
4 Number Sum
Function that takes in array and a target sum.
Returns a list of all quadruplets that add up to target sum.

Sample input: [7, 6, 4, -1, 1, 2], 16
Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]
'''

class Prob:
    @staticmethod
    def fourNumberSum(array, target):
        quads = []
        arraySorted = sorted(array)
        print("arraySorted: ", arraySorted)
        for i in range(len(array)-4):
            print("i= ", i)
            arraySection = arraySorted[i:]
            Prob.helper(arraySection, target, quads, 0, 1, 2, len(arraySection)-1)
        return quads
    
    @staticmethod
    def helper(arraySection, target, quads, i1, i2, i3, i4):
        print("helper: i1={}, i2={}, i3={}, i4={}".format(i1,i2,i3,i4))
        if i2 == i3 or i3 == i4:
            return
        
        v1 = arraySection[i1]
        v2 = arraySection[i2]
        v3 = arraySection[i3]
        v4 = arraySection[i4]
        arraySectionSum = v1 + v2 + v3 + v4
        print("v1={}, v2={}, v3={}, v4={}, sum={}".format(v1,v2,v3,v4,arraySectionSum))
        
        if arraySectionSum == target:
            quad = [v1,v2,v3,v4]
            if quad not in quads:
                quads.append([v1,v2,v3,v4])
                print("quads updated: ", quads)
        
        if arraySectionSum > target:
            print("A")
            Prob.helper(arraySection, target, quads, i1, i2, i3, i4-1)
        else:
            print("B")
            Prob.helper(arraySection, target, quads, i1, i2, i3+1, i4)
            Prob.helper(arraySection, target, quads, i1, i2+1, i3, i4)

    @staticmethod
    def test1():
        array = [7, 6, 4, -1, 1, 2]
        target = 16
        #target = 100
        quads = Prob.fourNumberSum(array, target)
        print("test1: quads final: ", quads)
    
    @staticmethod
    def test2():
        array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
        target = 30
        quads = Prob.fourNumberSum(array, target)
        print("test2: quads final: ", quads)

#Prob.test1()
Prob.test2()

