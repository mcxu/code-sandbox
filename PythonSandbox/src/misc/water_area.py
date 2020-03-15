'''
Water Area

Given array ints, each non-zero int represents the height of a pillar of width 1.
What is the total surface area (viewed from from) of the water that the space
between the pillars can hold?

Sample input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
Sample output: 48
'''

class Prob:
    '''
    Recursive brute force
    '''
    @staticmethod
    def waterArea(heights):
        MAXHEIGHTROOT = max(heights)
        MAXINDROOT = heights.index(MAXHEIGHTROOT)
        print("MAXINDROOT: ", MAXINDROOT)
        waterAmts = [0 for _ in heights]
        print("waterAmts: ", waterAmts)
        Prob.waterAreaHelper(heights, MAXINDROOT, waterAmts, left=True)
        Prob.waterAreaHelper(heights, MAXINDROOT, waterAmts, left=False)
        print("waterAmts after: ", waterAmts)
        return sum(waterAmts)
        
    '''
    left = True means this is for looking to the left subarray, False means to the right subarray
    '''
    @staticmethod
    def waterAreaHelper(heights, maxInd, waterAmts, left):
        print("maxInd: ", maxInd)
        if left == True:
            heightsLeft = heights[0:maxInd]
            print("heightsLeft: ", heightsLeft)
            
            # base case for left subarray: left subarray is empty
            if not heightsLeft: 
                return
            
            maxHeightLeft = max(heightsLeft)
            print("maxHeightLeft: ", maxHeightLeft)
            maxIndLeft = heightsLeft.index(maxHeightLeft)
            print("maxIndLeft: ", maxIndLeft)
            for i in range(maxIndLeft+1, maxInd):
                waterAmts[i] = maxHeightLeft - heights[i]
            Prob.waterAreaHelper(heights, maxIndLeft, waterAmts, left=True)
            
        if left == False:
            heightsRight = heights[maxInd+1:]
            print("heightsRight: ", heightsRight)
            
            # base case for right subarray: that right subarray is empty
            if not heightsRight: 
                return
            
            maxHeightRight = max(heightsRight)
            print("maxHeightRight: ", maxHeightRight)
            maxIndRight = heightsRight.index(maxHeightRight)
            print("maxIndRight: ", maxIndRight)
            for i in range(maxIndRight+maxInd, maxInd, -1):
                waterAmts[i] = maxHeightRight - heights[i]
            Prob.waterAreaHelper(heights, maxIndRight+maxInd+1, waterAmts, left=False)
    
    @staticmethod
    def test1(alg):
        heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
        #heights = [0, 8, 0, 0, 5, 9, 0, 10, 0, 0, 1, 1, 0, 3]
        #heights = [0, 9, 0, 0, 5, 8, 0, 10, 0, 0, 1, 1, 0, 3]
        print("heights: ", heights)
        res = alg(heights)
        print("test1 res: ", res)
    
    @staticmethod
    def test2(alg):
        #heights = [0,0,0] # res: 0 (correct)
        heights = [1,0,1] # incorrect
        res = alg(heights)
        print("test2 res: ", res)
    
    @staticmethod
    def test3(alg):
        heights = [0, 1, 0, 1, 0, 2, 0, 3]
        # correct ans: 4
        res = alg(heights)
        print("test3 res: ", res)
    
def main():
    alg1 = Prob.waterArea
    
    #Prob.test1(alg1)
    #Prob.test2(alg1)
    Prob.test3(alg1)

main()
