# https://leetcode.com/problems/palindrome-permutation-ii/

# Results in TLE
class Solution:
    def generatePalindromes(self, s: str) -> [str]:
        sList=list(s)
        #print("sList init: ", sList)
        perms = set()
        palPerms = []
        self.permute(sList, perms, palPerms)
        return palPerms
    
    def permute(self, sList, perms, palPerms):
        s = "".join(sList)
        if not s:
            return
        if s in perms:
            return
        else:
            perms.add(s)
            if s==s[::-1]:
                palPerms.append(s)
        
        for i in range(len(sList)-1):
            sList[i],sList[i+1] = sList[i+1],sList[i]
            self.permute(sList, perms, palPerms)
            sList[i],sList[i+1] = sList[i+1],sList[i]
        return

class Solution2:
    def generatePalindromes(self, s: str) -> [str]:
        res = []
        aux = {}
        odd = 0
        for _,ch in enumerate(s):
            if ch in aux.keys():
                aux[ch] += 1
            else:
                aux[ch] = 1
            
            if aux[ch]%2==1:
                odd += 1
            else:
                odd -= 1
        
        # print("aux: ", aux)
        # print("odd: ", odd)

        if len(s)==0 or odd > 1:
            return res
        
        pal = ""
        for k in aux.keys():
            if odd > 0 and aux[k]%2==1:
                pal += k
                aux[k] -= 1
                break
        print("pal: ", pal)
        
        n = len(s)
        self.helper(res, pal, aux, n)
        return res
    
    def helper(self, res, pal, aux, n):
        if len(pal)==n:
            res.append(pal)
            return
        print("helper: aux: ", aux)
        for k in aux.keys():
            if aux[k] > 0:
                aux[k] -= 2
                newpal = k+pal+k
                self.helper(res, newpal, aux, n)
                aux[k] += 2

sol = Solution2()
def test():
    s= "aabbc"
    res = sol.generatePalindromes(s)
    print("res: ", res)
test()