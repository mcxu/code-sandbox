"""
Determine the furthest 2 frogs can be from each other if:
- they can only jump to a higher step
- they start on the same step
"""

class Solution:
    def frogJump(self, steps):
        furthestDist = 0

        for startIdx in range(len(steps)):
            #print("startIdx: ", startIdx)
            i, j = startIdx, startIdx

            while i-1 >= 0 and steps[i-1] > steps[i]:
                i -= 1
            
            while j+1 <= len(steps)-1 and steps[j] < steps[j+1]:
                j += 1

            dist = j - i + 1
            furthestDist = max(furthestDist, dist)

        return furthestDist

    def test(self):
        #steps = [1,5,3,2,4,6] # expected 5 steps apart
        steps = [5,4,3,2,1,2,3,4,5] # expected 9 steps apart
        result = self.frogJump(steps)
        print("result: ", result)

s = Solution()
s.test()