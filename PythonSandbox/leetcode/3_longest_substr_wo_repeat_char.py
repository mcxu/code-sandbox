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

    # ===================================================================================
    # Solution using sliding window, which allows single pass

    def lengthOfLongestSubstring_slidingWindow(self, s: str, option: int = 1) -> int:
        longestSubstrLength = 0
        seen = set()
        indices = [0, 0] # [inclusive, exclusive]
        i, j = 0, 0
        while j < len(s):
            jval = s[j]
            if jval not in seen:
                seen.add(jval)
                j += 1

                if (option <= 1 or option >= 4):
                    longestSubstrLength = max(longestSubstrLength, j-i)
                elif option == 2:
                    # if you want indices
                    currLongest = longestSubstrLength
                    longestSubstrLength = max(longestSubstrLength, j-i)
                    if longestSubstrLength > currLongest:
                        indices = [i, j]
                        print("indices: ", indices)
                elif option == 3:
                    # if you want indices (another way)
                    currSpan = j-i
                    if currSpan > longestSubstrLength:
                        longestSubstrLength = currSpan
                        indices = [i, j]
                        print("indices: ", indices)
            else:
                seen.remove(s[i])
                i += 1
        
        return longestSubstrLength

    def test2(self):
        s = "abcabcbb"
        res = self.lengthOfLongestSubstring_slidingWindow(s, 1)
        print("res: ", res)
        assert res == 3


sol = Solution()
# sol.test1()
sol.test2()