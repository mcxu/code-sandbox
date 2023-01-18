class LC9_PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        if x == None:
            return False

        xstr = str(x)
        
        if xstr[0] == "-":
            return False

        i = 0
        j = len(xstr)-1
        while xstr[i] == xstr[j] and i < j:
            i += 1
            j -= 1
            
        if i >= j:
            return True

        return False

    
    def getTestCases(self):
        cases = { # expected values here
            121: True,
            -121: False,
            10: False
        }
        return cases

    def test1(self):
        for case, ans in self.getTestCases().items():
            res = self.isPalindrome(case)
            # print("res: ", res)
            assert res == ans

sol = LC9_PalindromeNumber()
sol.test1()