'''
Longest Palindromic Substring
Sample input: "abaxyzzyxf"
Sample output: "xyzzyx"
'''

class Prob:
    
    """
    Brute Force
    Let n = number chars in string
    Time complexity:
        O(n^2): for loops perform n(n-1)/2 iterations
        O(n): isPal function
        Total: O(n^3)
    Space complexity: O(1), since lPal stores only the largest palindrome.
    """
    @staticmethod
    def longestPalindromicSubstringBruteForce(string):
        lPal = "" # stores longest palendrome
        lLen = len(lPal)
        
        for i in range(len(string)): # O(n) time
            #print("----")
            for j in range(len(string), i, -1): # O(n^2) time
                #print("i={}, j={}".format(i,j))
                substr = string[i:j]
                #print("    substr: ", substr)
                subIsPal = Prob.isPal(substr) # O(n) time, O(1) space
                if subIsPal and len(substr) > lLen:
                    lPal = substr
                    lLen = len(lPal)
                    if i==0 and j==len(string):
                        return lPal
                        
        return lPal
    
    """
    let n = number chars in string
    Time complexity: O(n), since for loop iterates through at most n/2 elements
    Space complexity: O(1), since only string[i] and string[maxInd-i] are compared.
    """
    @staticmethod
    def isPal(string):
        maxInd = len(string)-1
        for i in range(int(len(string)/2)):
            if string[i] != string[maxInd-i]:
                return False
        return True
    
    @staticmethod
    def test_isPal():
        l1 = ['a','b','a']
        l2 = ['a','a','b','a']
        r1 = Prob.isPal(l1)
        print("r1: ", r1)
        r2 = Prob.isPal(l2)
        print("r2: ", r2)

    @staticmethod
    def test1():
        s1 = "abaxyzzyxf"; ans1 = "xyzzyx"
        s2 = "abaxyxa"; ans2 = "axyxa"
        s3 = "babab"; ans3 = "babab"
        s4 = "it's highnoon"; ans4 = "noon"
        s5 = "qwerty"
        s6 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        #cases = [s1, s2, s3, s4]
        cases = [s6]
        answers = [ans1, ans2, ans3, ans4]
        for case in cases:
            lpal = Prob.longestPalindromicSubstringBruteForce(case)
            print("test1: case: {},\nlpal: {}".format(case, lpal))

    
    @staticmethod
    def longestPalindromicSubstringExpansionMethod(string):
        j = 0 # keep track of start index of longest pal
        k = 0 # keep track of end index of longest pal
        lLen = 0
        
        for i in range(len(string)):
            #print("--- i=", i)
            plOdd = Prob.palLenExpansion(string, i, i) # len of palindrome w/ odd number of values
            plEven = Prob.palLenExpansion(string, i, i+1) # len of palindrom w/ even number of values
            #print("plOdd: {}, plEven: {}".format(plOdd, plEven))
            currLen = max(plOdd, plEven)
            #print("currLen: ", currLen)
            if currLen > lLen:
                j = i - int((currLen-1)/2)
                k = i + int(currLen/2)
                lLen = currLen
        
        return string[j:k+1] # k index is inclusive in terms of palindrome, so want to include kth value
            
    @staticmethod
    def palLenExpansion(string, i, j):
        while i >= 0 and j < len(string) and string[i] == string[j]:
            #print("isPalExpansion: i={}, j={}".format(i,j))
            #print("left: {}, right: {}".format(string[i], string[j]))
            i -= 1
            j += 1
        #print("isPalExpansion: final i={}, j={}".format(i,j))
        # return the start and end indices of the palindrome
        return (j-1)-(i-1)-1
    
    @staticmethod
    def test_palLenExpansion():
        s1 = "abaxyzzyxf"
        s2 = "aaabaaa"
        pl = Prob.palLenExpansion(s1,1,1)
        #pl = Prob.palLenExpansion(s1,5,6)
        #pl = Prob.palLenExpansion(s2,3,3)
        print("test_palLenExpansion: pl: ", pl)
        
    @staticmethod
    def test2():
        s1 = "abaxyzzyxf"; ans1 = "xyzzyx"
        s2 = "abaxyxa"; ans2 = "axyxa"
        s3 = "babab"; ans3 = "babab"
        s4 = "it's highnoon"; ans4 = "noon"
        s5 = "qwerty"
        s6 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        cases = [s1, s2, s3, s4, s5, s6]
        #cases = [s6]
        answers = [ans1, ans2, ans3, ans4]
        for case in cases:
            lpal = Prob.longestPalindromicSubstringExpansionMethod(case)
            print("test2: case: {},\nlpal: {}".format(case, lpal))
        
    
#Prob.test_isPal()
#Prob.test1()
#Prob.test_palLenExpansion()
Prob.test2()

 