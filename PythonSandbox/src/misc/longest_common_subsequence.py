'''
Longest common subsequence

Given 2 strings, implement function that returns longest subsequence
common to both strings. Subsequence values do not have to be adjacent,
but must be in terms of increasing index.

Sample input: "ZXVVYZW", "XKYKZPW"
Sample output: ["X", "Y", "Z", "W"]

Brute force complexity:
http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/DynProg/LCS-brute-force.html
'''

class Prob:
    '''
    Let l1=len(str1), l2=len(str2)
    Time complexity: O(l1*l2*min(l1,l2)), since nested for loops iterate through all l1*l2 char combinations.
        Additionally, for each cell, there can only be up to min(l1,l2) appends.
    Space complexity: O(l1*l2*min(l1,l2)). In addition to the matrix to store subsequence, the list in EACH cell
        adds min(l1,l2) characters to store. 
    '''
    @staticmethod
    def longestCommonSubsequence(str1, str2):
        # have a matrix to store LCS up to a coordinate
        subseqMatrix = [[[] for x in range(len(str1)+1)] for y in range(len(str2)+1)]
#         print("subseqMatrix")
#         for row in subseqMatrix: print(row)
        
        for y in range(1, len(str2)+1):
            for x in range(1, len(str1)+1):
                #print("---------------")
                #print("current corrdinates y={}, x={}".format(y,x))
                if str1[x-1] == str2[y-1]:
                    # case1: find matching chars in lists
                    # action: set cell [y,x] to the upper left diagonal cell [y-1,x-1] joined with matching char, forming a subsequence
                    #print("found match at str2[{}]={}, str1[{}]={}".format(y-1, str2[y-1], x-1, str1[x-1]))
                    subseqMatrix[y][x] = subseqMatrix[y-1][x-1] + [str1[x-1]]
                    
                elif len(subseqMatrix[y][x-1]) >= len(subseqMatrix[y-1][x]):
                    # case2: for coord [y,x], the subsequence in the cell to the left longer than the cell above
                    # action: set cell [y,x] to whatever is in the cell to the left
                    subseqMatrix[y][x] = subseqMatrix[y][x-1]
                     
                elif len(subseqMatrix[y-1][x]) > len(subseqMatrix[y][x-1]):
                    # case3: for coord [y,x], the subsequence in the cell above longer than cell to left
                    # action set cell [y,x] to whatever is in the cell above
                    subseqMatrix[y][x] = subseqMatrix[y-1][x]
                
                #The above 2 elifs can be condensed into this else logic:
#                 else:
#                     subseqMatrix[y][x] = max(subseqMatrix[y][x-1], subseqMatrix[y-1][x])
                
                print("subseqMatrix (debug):")
                for row in subseqMatrix: print(row)
        
        return subseqMatrix[len(str2)][len(str1)]


    '''
    This version uses pointers to point to the previous LCS solution for some given char combination.
    Let l1=len(str1), l2=len(str2)
    Time complexity: O(l1*l2) for nested y and x for loops. 
        Within nested for loops 2*O(1) to update lcsLengthMatrix and pointerMatrix, respectively.
        Backtrack takes max(l1,l2) time.
        Total time complexity = O(l1*l2) * 2O(1) + O(max(l1,l2)) = 2*O(l1*l2) = O(l1*l2)
    Space complexity: lcsLengthMatrix = O(l1*l2), pointerMatrix = O(l1*l2), both is still O(l1*l2).
    '''
    @staticmethod
    def longestCommonSubsequenceUsingPointer(str1, str2):
        # stores the lengths of solutions up to the current coordinate
        # str1: horizontal axis (x), str2: vertical axis (y)
        lcsLengthMatrix = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
        
        '''
        Stores the pointers that point back to the latest solution up to the current coordinate
        The key below makes a path to the LCS for the combo of the last characters in str1 and str2.
        \    (put this in the cell when a match is found, means to examine further down both strings)
        --   (put this in the cell when for some cell [y,x], cell to left >= cell above, means to move to the next char in str1 (x-axis)
        |    (put this in the cell when for some cell [y,x], cell above > cell to left, means to move the next char in str2 (y-axis)
        '''
        pointerMatrix = [[None for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
        
        for y in range(1, len(str2)+1):
            for x in range(1, len(str1)+1):
                print("y={} -> {}, x={} -> {}".format(y,str2[y-1],x,str1[x-1]))
                if str1[x-1] == str2[y-1]:
                    lcsLengthMatrix[y][x] = lcsLengthMatrix[y-1][x-1] + 1
                    pointerMatrix[y][x] = '\\'
                elif lcsLengthMatrix[y][x-1] >= lcsLengthMatrix[y-1][x]: # left >= above
                    lcsLengthMatrix[y][x] = lcsLengthMatrix[y][x-1]
                    pointerMatrix[y][x] = '--'
                elif lcsLengthMatrix[y][x-1] < lcsLengthMatrix[y-1][x]: # left < above
                    lcsLengthMatrix[y][x] = lcsLengthMatrix[y-1][x]
                    pointerMatrix[y][x] = ' |'
        
                print("printing pointerMatrix:")
                for row in pointerMatrix: print(row)
        
        # backtrack using pointerMatrix
        lcs = []
        Prob.backtrack(pointerMatrix, len(str2), len(str1), str2, lcs)
        return lcs
                    
    @staticmethod
    def backtrack(pointerMatrix, y, x, str2, lcs):
        if y==None or x==None:
            return
        
        currSymbol = pointerMatrix[y][x]
        if currSymbol == '\\':
            # this symbol means matching chars were found, so insert it to the lcs list
            # need insertion because backtracking means you will find answer in reverse
            lcs.insert(0, str2[y-1])
            # backtrack 1 cell along y-axis, and 1 cell along x-axis
            Prob.backtrack(pointerMatrix, y-1, x-1, str2, lcs)
        elif currSymbol == ' |':
            # backtrack along y-axis 1 cell
            Prob.backtrack(pointerMatrix, y-1, x, str2, lcs)
        elif currSymbol == '--':
            # backtrack along x-axis 1 cell
            Prob.backtrack(pointerMatrix, y, x-1, str2, lcs)
            
    @staticmethod
    def test1(alg):
        str1 = "ZXVVYZW"
        str2 = "XKYKZPW"
        lcs = alg(str1, str2)
        print("test1: lcs: ", lcs)
        
    @staticmethod
    def test2(alg):    
        #str1 = "ABCBDAB"; str2 = "BDCABA";
        str1 = "101"; str2 = "100010101";
        lcs = alg(str1, str2)
        print("test2: lcs: ", lcs)

    @staticmethod
    def test3(alg):
        str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str2 = "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAG"
        # ans: ['C', 'D', 'E', 'G', 'H', 'J', 'K', 'L', 'W']
        lcs = alg(str1, str2)
        print("test3: lcs: ", lcs)

    @staticmethod
    def test4(alg):
        str1 = "AAA"
        str2 = "AAAAAAAAAAAAAAAAAA"
        lcs = alg(str1, str2)
        print("test4: lcs: ", lcs)

    @staticmethod
    def test5(alg):
        str1 = "ABC"
        str2 = "ABCDEFG"
        lcs = alg(str1, str2)
        print("test5: lcs: ", lcs)
        
def main():
    alg1 = Prob.longestCommonSubsequence
    alg2 = Prob.longestCommonSubsequenceUsingPointer
    
    #Prob.test1(alg2)
    #Prob.test2(alg2)
    #Prob.test3(alg2)
    #Prob.test4(alg2)
    Prob.test5(alg2)

main()


