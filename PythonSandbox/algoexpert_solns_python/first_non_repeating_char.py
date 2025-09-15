'''
Find 1st non-repeating char in string.
'''
class Solution:
    def firstNonRepeatChar(self, s):
        freqMap = {}
        sequence = [] # stores unique chars, in order which they appear in s
        for i,v in enumerate(s):
            if v in freqMap.keys():
                freqMap[v] += 1
            else:
                freqMap[v] = 1
                sequence.append(v)
        
        for c in sequence:
            if freqMap[c] == 1:
                return c
        return None
    
    def test1(self):
        #s = "aaabcccdeeef"
        #s = "aabbcc"
        s = "aaaaaaabbbcdef"
        res = self.firstNonRepeatChar(s)
        print("res: ", res)

sol = Solution()
sol.test1()