# https://leetcode.com/problems/remove-k-digits/

# better solution 


# results in TLE
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        smallest = [float('inf')]
        numList=list(num)
        self.helper(numList, k, 0, smallest)
        if smallest[0]==float('inf') and k != 0:
            return "0"
        elif k==0:
            return str(num)
        return str(smallest[0])
    
    def helper(self, numList, k, i, smallest):
        if k==0:
            return
        if i > len(numList)-1:
            return
        
        # remove
        removedVal = numList[i]
        numList[i] = ""
        
        # test
        numListJoined = "".join(numList)
        if not numListJoined:
            smallest[0] = 0
            return
        
        currVal = int(numListJoined)
        if currVal < smallest[0]:
            smallest[0] = currVal
        
        # recurse for case where val at current index is removed
        self.helper(numList, k-1, i+1, smallest)
        
        # replace
        numList[i] = removedVal
        # recurse for case where val at current index is NOT removed
        self.helper(numList, k, i+1, smallest)