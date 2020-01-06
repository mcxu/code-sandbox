"""
Function that takes 2 strings, return the minimum number of edit
operations that need to be performed on the 1st string to get the 2nd string.
Valid operations are: insertion, deletion, substitution, of a character.

Sample input: "abc", "yabd"
Sample output: 2 (insert "y", subsitute "c" for "d")
"""

class Prob:
    @staticmethod
    def levenshteinDistance(str1, str2):
        # 2d array to store number of ops
        ops = [[-1 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        print("ops: ", ops)
        
        # populate null row and column (convention from row to column)
        ops[0] = [i for i in range(len(str1)+1)]
        for i in range(1, len(ops)):
            ops[i][0] = i
        print("ops after init: ", ops)
        
        # iterate through each subproblem in the 2d array
        for i in range(1, len(ops)):
            for j in range(1, len(ops[i])):
                print("i= %d, j= %d" % (i, j),)
                
                fromChar = str1[j-1]
                toChar = str2[i-1]
                print("    fromChar: %s, toChar: %s" % (fromChar, toChar))
                
                replace = ops[i-1][j-1]
                delete = ops[i-1][j]
                insert = ops[i][j-1]
                print("    replace: %s, delete: %s, insert: %s" % (replace, delete, insert))
                
                if fromChar == toChar:
                    ops[i][j] = replace
                else:
                    ops[i][j] = min(replace, delete, insert) + 1
        
        print("ops final: ", ops)
        return ops[len(str2)][len(str1)]

    @staticmethod
    def test1():
        minDist = Prob.levenshteinDistance("abc", "yabd")
        print("test1: minDist: ", minDist)

Prob.test1()