class PalindromeCheck:
    @staticmethod
    def palindromeCheck(s):
        isPal = True
        for i in range(int(len(s)/2)):
            loChar = s[i]
            hiChar = s[len(s)-1-i]
            if loChar != hiChar:
                isPal = False
        return isPal
    
    @staticmethod
    def test_palindromeCheck():
        s = ["abcba",
             "bbbb",
             "a",
             "bbas"]
        for elt in s:
            b = PalindromeCheck.palindromeCheck(elt)
            print("Result for {}: {}".format(elt, b))

def main():
    PalindromeCheck.test_palindromeCheck()

main()