'''
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values. Return the minimum number of rotations 
so that all the values in A are the same, or all the values in B are the same. If it cannot be done, return -1.
'''
class Solution:
    '''
    4 possibilities:
    - All values in A match A[0]
    - All values in A match B[0]
    - All values in B match A[0]
    - All values in B match B[0]
    Let n = len(A) (len(B) is same)
    Time complexity: 
    '''
    def minDominoRotations2(self, A: [int], B: [int]) -> int:
        # All values in A match A[0]
        AMatchA0 = self.numSwaps(A,B,A[0])
        print("AMatchA0:", AMatchA0)
        # All values in A match B[0]
        AMatchB0 = self.numSwaps(A,B,B[0])
        print("AMatchB0:", AMatchB0)
        # All values in B match A[0]
        BMatchA0 = self.numSwaps(B,A,A[0])
        print("BMatchA0:", BMatchA0)
        # All values in B match B[0]
        BMatchB0 = self.numSwaps(B,A,B[0])
        print("BMatchB0:", BMatchB0)
        
        minSwapsToMatchA0 = min(AMatchA0, BMatchA0)
        minSwapsToMatchB0 = min(AMatchB0, BMatchB0)
        minSwapsOverall = min(minSwapsToMatchA0, minSwapsToMatchB0)
        print("minSwapsOverall: ", minSwapsOverall)
        if minSwapsOverall == float('inf'):
            return -1
        return minSwapsOverall
        
    # Tally of all values in array A that match some value.
    def numSwaps(self, A, B, matchVal):
        numSwaps = 0
        for i in range(len(A)):
            if A[i] != matchVal and B[i] != matchVal:
                return float('inf')
            elif A[i] != matchVal and B[i] == matchVal:
                numSwaps += 1
        return numSwaps


    # --------------------------------------------------------------------

    # Generating a tree of permutations: Time limit exceeded
    def minDominoRotations(self, A: [int], B: [int]) -> int:
        swapPositions = [0 for _ in A]
        spList = []
        self.helper(A, B, len(A)-1, swapPositions, spList)
        print("spList after helper: ", spList)
        
        swapCountList = [sum(x) for x in spList]
        if swapCountList:
            return min(swapCountList)
        return -1

    def helper(self, A, B, i, swapPositions, spList):
        print("i=", i)
        print("A: {}\nB: {}".format(A, B))
        print("swapPositions:", swapPositions)
        
        if i < 0:
            return

        if len(set(A)) == 1 or len(set(B)) == 1:
            spCopy = swapPositions.copy()
            if spCopy not in spList:
                print("appending to spList: ", spCopy)
                spList.append(spCopy)

        # not swap
        self.helper(A,B,i-1,swapPositions,spList)

        # do a swap
        if A[i] != B[i]:
            A[i],B[i] = B[i],A[i]
            swapPositions[i] = 1
            self.helper(A, B, i-1, swapPositions,spList)
            # need to swap back b/c the next child swap needs the original state.
            A[i],B[i] = B[i],A[i]
            swapPositions[i] = 0


    def test1(self, alg):
        A = [2,1,2,4,2,2]
        B = [5,2,6,2,3,2]
        # expected: 2
        res = alg(A,B)
        print("test1 res: ", res)

    def test2(self,alg):
        A = [3,5,1,2,3]
        B = [3,6,3,3,4]
        #expected: -1
        res = alg(A,B)
        print("test2 res: ", res)

    def test3(self,alg):
        A = [1,1,1,1,1,1,1,1,1,1,1]
        B = [1,1,1,1,1,1,1,1,1,1,1]
        res = alg(A,B)
        print("test3 res: ", res)

    def test4(self,alg):
        A = [1,1,1,2,2,2,1]
        B = [2,2,1,1,1,1,2]
        res = alg(A,B)
        print("test4 res: ", res)

    def test5(self,alg):
        A = [3,5,1,2,3]
        B = [3,6,3,3,4]
        # expected -1
        res = alg(A,B)
        print("test5 res: ", res)

s = Solution()
# alg = s.minDominoRotations
alg = s.minDominoRotations2
#s.test1(alg)
#s.test2(alg)
#s.test3(alg)
#s.test4(alg)
s.test5(alg)