'''
Disk Stacking: Given a list of disks with [width, depth, height].
Write function to stack the disks from bottom (last element) to top (0th element) so that
each disks has strictly smaller width, depth, height than the disks below it.

Sample:
input = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
output = [[2, 1, 2], [3, 2, 3], [4, 4, 5]]
([2,1,2] is top disk, [4,4,5] is bottom disk)
'''

class Prob:
    @staticmethod
    def stackDisksBruteForce(disks):
        # stackMap format: 
        # total height of stack : [[stack1], [stack2], etc.]
        stackMap = {}

        # sort disks by height
        disksSortedByHeight = sorted(disks, key=lambda x: x[2]) # O(nlogn) time
        print("disksSortedByHeight:", disksSortedByHeight)

        for i in range(len(disksSortedByHeight)-1, -1, -1):
            
            currStartingDisk = disksSortedByHeight[i]
            print("currStartingDisk:", currStartingDisk)
            currStartingDiskHeight = currStartingDisk[2]
            if currStartingDiskHeight not in stackMap.keys():
                stackMap[currStartingDiskHeight] = [[currStartingDisk]]
            #print("stackMap: ", stackMap)

            for j in range(i, -1, -1):
                newStackFromCurr = [currStartingDisk] # from curr down to index 0
                currStartingDiskWidth = currStartingDisk[0]
                currstartingDiskDepth = currStartingDisk[1]
                prevDiskTmp = currStartingDisk # for comparison
                for k in range(j-1, -1, -1):
                    print("i={}, j={}, k={}".format(i,j,k))
                    print("prevDiskTmp: ", prevDiskTmp)
                    nextDiskForNewStack = disksSortedByHeight[k]
                    print("nextDiskForNewStack: ", nextDiskForNewStack)
                    nextDiskWidth = nextDiskForNewStack[0]
                    nextDiskDepth = nextDiskForNewStack[1]
                    prevDiskWidth = prevDiskTmp[0]
                    prevDiskDepth = prevDiskTmp[1]
                    if (nextDiskWidth < prevDiskWidth) and (nextDiskDepth < prevDiskDepth) and \
                        (nextDiskWidth < currStartingDiskWidth) and (nextDiskDepth < currstartingDiskDepth):
                        print("     inserting: ", nextDiskForNewStack)
                        newStackFromCurr.insert(0, nextDiskForNewStack)
                        prevDiskTmp = nextDiskForNewStack
                print("newStackFromCurr: ", newStackFromCurr)
                stackHeight = Prob.getStackHeight(newStackFromCurr)
                if stackHeight in stackMap.keys():
                    if newStackFromCurr not in stackMap[stackHeight]:
                        stackMap[stackHeight].append(newStackFromCurr)
                else:
                    stackMap[stackHeight] = [newStackFromCurr]
        
        print("\nstackMap after: ")
        for key in stackMap.keys():
            print("key: {}, stacks: {}".format(key, stackMap[key]))
        
        tallestValidStack = stackMap[max(stackMap.keys())][0]
        return tallestValidStack

    # returns total height of stack         
    @staticmethod
    def getStackHeight(stack):
        totHeight = 0
        for disk in stack:
            totHeight += disk[2]
        return totHeight


    @staticmethod
    def test1(alg):
        input = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
        output = alg(input)
        print("test1 output: ", output)
    
    @staticmethod
    def test2(alg):
        input = [[2, 1, 2], [3, 2, 3], [2, 2, 8]] # Expected: [[2, 2, 8]]
        output = alg(input)
        print("test2 output: ", output)

    @staticmethod
    def test3(alg):
        input = [[2, 1, 2], [3, 2, 5], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
        output = alg(input)
        print("test3 output: ", output)

alg = Prob.stackDisksBruteForce

#Prob.test1(alg)
#Prob.test2(alg)
Prob.test3(alg)