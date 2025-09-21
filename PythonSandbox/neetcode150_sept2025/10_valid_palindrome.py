class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            iVal = s[i]
            jVal = s[j]

            if (iVal.isalnum() and jVal.isalnum()):
                if iVal.lower() == jVal.lower():
                    i += 1; j -= 1
                else:
                    return False
            elif iVal.isalnum() and not jVal.isalnum():
                j -= 1
            elif not iVal.isalnum() and jVal.isalnum():
                i += 1
            else:
                i += 1; j -= 1
        
        return True
    
    def test_1(self):
        test_cases = [
            ["A man, a plan, a canal: Panama", True],
            ["race a car", False],
            [" ", True],
            [".,", True]
        ]

        for tc in test_cases:
            s, expected = tc[0], tc[1]
            print(f"===\nTest: {s}, \nExpected: {expected}")
            output = self.isPalindrome(s)
            print("output", output)
            assert output == expected

if __name__ == "__main__":
    cl = ValidPalindrome()
    cl.test_1()