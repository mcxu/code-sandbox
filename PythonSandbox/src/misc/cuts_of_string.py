'''
Given string s, find the number of ways that s can be cut.
Example: given "abc"
Return: 4
Cuts are:
['abc'] (the string itself counts as a cut)
['ab','c'],
['a,'b','c'],
['a','bc']
'''
class Solution:
    # include the string itself as a cut
    def numCutsIncludeS(self, s):
        i = len(s)-1
        return self.numCutsHelper(i)

    def numCutsHelper(self, i):
        if i == 0:
            return 1

        waysCut = self.numCutsHelper(i-1)
        waysNotCut = self.numCutsHelper(i-1)
        return waysCut + waysNotCut
    
    def test_numCutsIncludeS(self):
        #s="abcde" # return 16
        #s = "abcd" # return 8
        #s = "abc" # abc, a|bc, ab|c, a|b|c are cuts, return 4
        #s = "ab" # ab and a|b are cuts, return 2
        s = "a" # begin on i=0 -> return 1 (base case test)
        res = self.numCutsIncludeS(s)
        print("res: ", res)
    
    # =============================================================
    # Variation where the string itself is not included in
    # the number of cuts.
    def numCutsExcludeS(self, s):
        i = len(s)-1
        return self.numCutsHelper2(i)
    
    def numCutsHelper2(self, i):
        if i == 0:
            # If s was just 1 char, then there are no cuts.
            return 0
        
        # If s was 2 chars, there is 1 cut: 0 + 1
        waysCut = self.numCutsHelper2(i-1) + 1
        waysNotCut = self.numCutsHelper2(i-1)
        return waysCut + waysNotCut

    def test_numCutsExcludeS(self):
        #s="abcde" # return 15
        #s = "abcd" # return 7
        #s = "abc" # a|bc, ab|c, a|b|c are cuts, return 3
        #s = "ab" # ab and a|b are cuts, return 1
        s = "a" # begin on i=0 -> return 0 (base case test)
        res = self.numCutsExcludeS(s)
        print("res: ", res)

    # =============================================================
    '''
    Version where the program returns the cuts. Assume s itself is a cut.
    '''
    def getCuts(self, s):
        cuts = []
        if not s:
            return cuts
        cuts.append([s])
        currcut = []
        self.cutHelper(s, len(s)-1, currcut, cuts)
        return cuts

    def cutHelper(self, s, i, currcut, cuts):
        #print("i={}, currcut: {}".format(i, currcut))
        if i == 0:
            if len(currcut)>0 and currcut not in cuts:
                cuts.append(currcut)
            return
        elif not s:
            return
        
        # cut
        precut = s[:i]
        postcut = s[i:]
        newcut = [precut,postcut]
        for j in range(1, len(currcut)):
            newcut.append(currcut[j]) # add the rest (starting from index 1) of the current cut to the new cut.
        #print(" prefSuf after: ", prefSuf)
        self.cutHelper(precut, i-1, newcut, cuts)

        # not cut
        self.cutHelper(s, i-1, currcut, cuts)


    def test_getCuts(self):
        #s = "a"
        #s = "ab"
        s = "abc"
        #s = "abcd"
        #s = "abcdefghi"
        res = self.getCuts(s)
        print("res: ", res)
        print("number of unique cuts: ", len(res))


sol = Solution()
#sol.test_numCutsIncludeS()
#sol.test_numCutsExcludeS()
sol.test_getCuts()