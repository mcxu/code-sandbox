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
    @staticmethod
    def longestCommonSubsequence(str1, str2):
        # have a matrix to store LCS up to a coordinate
        subseqMatrix = [[[] for x in range(len(str1)+1)] for y in range(len(str2)+1)]
#         print("subseqMatrix")
#         for row in subseqMatrix: print(row)
        
        list1 = list(str1)
        list2 = list(str2)
        
        for y in range(1, len(list2)+1):
            for x in range(1, len(list1)+1):
                #print("---------------")
                #print("current corrdinates y={}, x={}".format(y,x))
                if list1[x-1] == list2[y-1]:
                    # case1: find matching chars in lists
                    # action: set cell [y,x] to the upper left diagonal cell [y-1,x-1] joined with matching char, forming a subsequence
                    #print("found match at str2[{}]={}, str1[{}]={}".format(y-1, str2[y-1], x-1, str1[x-1]))
                    subseqMatrix[y][x] = subseqMatrix[y-1][x-1] + [list1[x-1]]
                    
                elif len(subseqMatrix[y][x-1]) >= len(subseqMatrix[y-1][x]):
                    # case2: for coord [y,x], the subsequence in the cell to the left longer than the cell above
                    # action: set cell [y,x] to whatever is in the cell to the left
                    subseqMatrix[y][x] = subseqMatrix[y][x-1]
                    
                elif len(subseqMatrix[y-1][x]) > len(subseqMatrix[y][x-1]):
                    # case3: for coord [y,x], the subsequence in the cell above longer than cell to left
                    # action set cell [y,x] to whatever is in the cell above
                    subseqMatrix[y][x] = subseqMatrix[y-1][x]
                
#                 print("subseqMatrix (debug):")
#                 for row in subseqMatrix: print(row)
        
        return subseqMatrix[len(str2)][len(str1)]
        
    @staticmethod
    def test1():
        str1 = "ZXVVYZW"
        str2 = "XKYKZPW"
        lcs = Prob.longestCommonSubsequence(str1, str2)
        print("test1: lcs: ", lcs)
        
    @staticmethod
    def test2():    
        #str1 = "ABCBDAB"; str2 = "BDCABA";
        str1 = "101"; str2 = "100010101";
        lcs = Prob.longestCommonSubsequence(str1, str2)
        print("test2: lcs: ", lcs)

    @staticmethod
    def test3():
        str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str2 = "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAG"
        lcs = Prob.longestCommonSubsequence(str1, str2)
        print("test3: lcs: ", lcs)

#Prob.test1()
#Prob.test2()
Prob.test3()

