''' two pointer method '''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0; j=len(s)-1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()==s[j].lower():
                    i+=1; j-=1
                else:
                    return False
            elif s[i].isalnum() and not s[j].isalnum():
                j-=1
            elif not s[i].isalnum() and s[j].isalnum():
                i+=1
            elif not s[i].isalnum() and not s[j].isalnum():
                i+=1; j-=1
        return True

''' filter, then 2 pointer via for loop '''
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        sList = [c.lower() for _,c in enumerate(s) if c.isalnum()]

        for i in range(len(sList)//2):
            c = sList[i]
            c2 = sList[len(sList) - 1 - i]
            if c != c2:
                return False

        return True

class Solution3:
    
    