'''
917. Palindrome Permutation II
https://www.lintcode.com/problem/palindrome-permutation-ii/description

Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.
Input: s = "aabb"
Output: ["abba","baab"]

Input: "abc"
Output: []
'''
import time
class Prob:
    @staticmethod
    def palindromePerms(s):

        def helper(sList, permList, palPermList):
            sListStr = "".join(sList)
            if sListStr in permList:
                return 
            else:
                permList.append(sListStr)
                if Prob.isPal(sListStr):
                    palPermList.append(sListStr)

            for i in range(len(sList)-1):
                Prob.swap(sList, i, i+1)
                helper(sList, permList, palPermList)
                Prob.swap(sList, i, i+1)
            return 

        permList = []
        palPermList = []
        helper(list(s), permList, palPermList)
        return palPermList


    @staticmethod
    def swap(sList, i, j):
        sList[i], sList[j] = sList[j], sList[i]
    
    @staticmethod
    def isPal(s):
        for i in range(int((len(s)-1)/2)+1):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    @staticmethod
    def test_isPal():
        s1 = "aaabbbaaa"
        s2 = "abab"
        res1 = Prob.isPal(s1)
        print("res1: ", res1)
        res2 = Prob.isPal(s2)
        print("res2: ", res2)

    @staticmethod
    def test1():
        #s1 = "baa"
        #s1 = "aaabbabaab"
        s1 = "abc"
        res = Prob.palindromePerms(s1)
        print("test1 res:", res)

#Prob.test_isPal()
Prob.test1()