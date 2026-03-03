'''
https://leetcode.com/problems/valid-palindrome-ii/
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note: The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution:
    '''
    Let n = len(s)
    Time: 
        If s is already pal, then O(n) time because i,j will meet at middle.
        If s is not pal, then from where s[j]!=s[j], isPal is run with rest of array, twice. O(n)
        So total time complexity: O(n)
    Space:
        O(1), since i,j,lo,hi are only pointers throughout array s.
    '''
    def validPalindrome(self, s):
        def isPal(s, lo, hi):
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo+=1
                hi-=1
            return True

        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                # remove ith value, like checking if values in range [i+1, j] inclusive, is pal
                deletei = isPal(s, i+1, j)
                # remove jth value, like checking if values in range [i, j-1] inclusive, is pal
                deletej = isPal(s, i, j-1)
                # reasoning: If s[i]!=s[j], then if [i+1,j] (remove ith val) or [i,j-1] (remove jth val) 
                # is still not pal, then you know you cannot just remove at most 1 val to make it a pal.
                if deletei or deletej:
                    return True
                else:
                    return False
        # at this point, i=j if whole string is pal, which will eval to true
        return s[i]==s[j]

    '''
    Brute Force: Time limit exceeded (initial attempt)
    Let n = len(s)
    Time: O(n^2): outer for loop iterating through n elements, inner while loop iterating through int(n/2) elements.
    Space: O(1): no new string is being created, only using pointers i,j,k.
    '''
    def validPalindromeBF(self, s):
        def isPal(i, s):
            j = 0
            k = len(s)-1
            while j < k:
                if j == i:
                    j+=1
                elif k == i:
                    k-=1
                if s[j] != s[k]:
                    return False
                j+=1; k-=1
            return True

        for i in range(len(s)):
            res = isPal(i, s)
            if res:
                return res
        return False

    def test1(self, alg):
        #s = "aba"
        #s = "abca"
        s = "abac"
        #s = "abdab"
        res = alg(s)
        print("res: ", res)
    
s = Solution()
#alg = s.validPalindromeBF
alg = s.validPalindrome
s.test1(alg)