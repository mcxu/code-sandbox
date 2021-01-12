# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestIndLength = 0 # length, the actual indices
        for k in range(len(s)):
            (i,j) = self.expansionCheckForRepeatChar(s, k) # (i inclusive, j exclusive)
            #print("indices: ", (i,j))
            indLength = j-i
            if indLength > longestIndLength:
                longestIndLength = indLength
        
        #print("longestIndLength: ", longestIndLength)
        return longestIndLength
    
    # returns the indices corresponding to the longest substring without repeating char    
    def expansionCheckForRepeatChar(self, s, i):
        covered = set(s[i])
        #print("covered: ", covered)
        j = i+1
        while j < len(s):
            #print("i={}, j={}".format(i, j))
            #print("covered: ", covered)
            if s[j] in covered:
                break
            else:
                covered.add(s[j])
                
            j += 1
        
        return (i,j)
    
    def test1(self):
        #s = "abcabcbb"
        #s = "bbbbb"
        #s = "au"
        s = "pwwkew"
        length = self.lengthOfLongestSubstring(s)
        print("test1 length: ", length)

sol = Solution()
sol.test1()