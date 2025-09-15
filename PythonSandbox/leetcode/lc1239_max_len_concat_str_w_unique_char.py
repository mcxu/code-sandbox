'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
# Recursive Solution
class Solution_Recursive:
    def maxLength(self, arr: [str]) -> int:
        maxLen = [0]
        for i in range(len(arr)):
            sInit = arr[i]
            self.helper(arr, i, sInit, maxLen)
        return maxLen[0]    
        
    def helper(self, arr, i, sInit, maxLen):
        if i > len(arr)-1:
            return
        
        if len(set(list(sInit)))==len(sInit) and len(sInit)>maxLen[0]:
            maxLen[0] = len(sInit)
        
        self.helper(arr, i+1, sInit, maxLen) # not concat
        if i+1 <= len(arr)-1:
            self.helper(arr, i+1, sInit+arr[i+1], maxLen) # concat

# Iterative Solution
class Solution_Iterative:
    def maxLength(self, arr: [str]) -> int:
        # powerset generation time complexity: O(n*2^n)
        arrIdPowerset = [[]]
        for i,_ in enumerate(arr):
            for j in range(len(arrIdPowerset)):
                subset = arrIdPowerset[j] + [i]
                arrIdPowerset.append(subset)
        #print("arrIdPowerset: ", arrIdPowerset)
        
        maxLen = 0
        for i in range(1, len(arrIdPowerset)):
            subset = arrIdPowerset[i]
            cc = ""
            for j in range(len(subset)):
                cc += arr[subset[j]]
            
            ccSet = set(list(cc))
            ccLen = len(cc)
            if len(ccSet)==ccLen and ccLen>maxLen:
                maxLen = ccLen
        return maxLen