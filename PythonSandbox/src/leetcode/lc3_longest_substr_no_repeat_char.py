'''
3. Longest Substring Without Repeating Characters

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestIndLength = [0, None] # length, the actual indices
        for k in range(len(s)):
            (i,j) = self.expansionCheckForRepeatChar(s, k) # (i inclusive, j exclusive)
            print("indices: ", (i,j))
            indLength = j-i
            if indLength > longestIndLength[0]:
                longestIndLength[0] = indLength
                #longestIndLength[1] = (i,j) # dont need since question asks for just length
        
        print("longestIndLength: ", longestIndLength)
        return longestIndLength[0]
    
    # returns the indices corresponding to the longest substring without repeating char    
    def expansionCheckForRepeatChar(self, s, i):
        covered = set(s[i])
        print("covered: ", covered)
        j = i+1
        while j < len(s):
            print("i={}, j={}".format(i, j))
            print("covered: ", covered)
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